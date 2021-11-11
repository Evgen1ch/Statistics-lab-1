import numpy as np
import numpy.linalg as linalg
import scipy.stats as sts

def weib(x, a, b):
    return (1.0 - np.exp(-(x**b / a)))

def weib_density(x,a,b):
    return (b/a)*(x**(b-1))*np.exp(-(x**b)/a)

def restore_veibull_distribution(data, cdf, error=0.05):
    #
    # F(x) = 1 - exp(-(x^β / α))
    # f(x) = 
    #
    # ti = log(xi)
    # b = β
    # a = -ln(α) => α = exp(-a)
    # 
    #
    # approximation of line bt + a
    #      N-1
    # RSS = Σ (b*ti + a - yi)^2 -> min
    #      i=1
    #
    # S2 = RSS / N - 3                              <- dispersion of distances
    #
    #      / Σti^2  Σti \          / Σyi*ti  Σti \
    # A = |             |    A1 = |              |
    #     \  Σti    N-1/          \  Σyi     N-1/
    #
    # b = determinant(A1) / determinant(A) = ((N-1) * Σyi*ti - Σyi * Σti) / ((N-1) * Σti^2 - (Σti)^2)
    #
    # a = (Σyi - b * Σti) / (N - 1)
    #
    # DC = S2 * A^-1
    #
    # Dispersion(b) = DC[0][0]
    # Dispersion(a) = DC[1][1]
    #
    # Confidence intervals calculated by formula: [θ - t(.975, N-3) * Dispersion(θ) ; θ + t(.975, N-3) * Dispersion(θ)], θ = a, b
    # t - quantile of Student`s t distribution

    x = data
    y = cdf
    N = len(x)

    y = np.log(np.log(1.0 / (1.0 - y)))
    t = np.log(x)
    
    sumt = np.sum(t)
    sumy = np.sum(y)
    sumt2= np.sum(t*t)
    sumty = np.sum(t*y)

    b = (N * sumty - sumy * sumt) / (N * sumt2 - sumt ** 2)
    a = (sumy - b * sumt) / N 
    a = np.exp(-a)      # a = -ln(a) => a = e^-a

    #calculating confidence intervals
    squares = (b * t + a - y)**2
    SS = np.sum(squares) / (N - 2)
    DC = SS * linalg.inv(np.array([[N, sumt],[sumt, sumt2]]))

    dispersion_b = DC[0][0]
    dispersion_a = DC[1][1]

    t = sts.t.ppf(1.0 - error / 2.0, df=N)
    stdb = np.sqrt(dispersion_b)
    stda = np.sqrt(dispersion_a)
    confidence_interval_b = (b - t * stdb, b + t * stdb)
    confidence_interval_a = (a - t * stda, a + t * stda)
    return a, b, confidence_interval_a, confidence_interval_b

def chi_square_test(x, a, b, error, bins):
    N = len(x)
    hist, edges = np.histogram(x, bins=bins)
    obs_freq = hist
    exp_freq = []

    for i in range(len(edges)-1):
        next = weib(edges[i+1], a, b)
        cur = weib(edges[i], a, b)
        theoretical_prob = (next - cur) * N
        exp_freq.append(theoretical_prob)

    chi2 = np.sum(((obs_freq - exp_freq)**2) / exp_freq)
    crit_chi2 = sts.chi2.ppf(1.0-error, df=bins)
    if(chi2 <= crit_chi2):
        return (True, chi2, crit_chi2)
    return (False, chi2, crit_chi2)
