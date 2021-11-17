import numpy as np

def Mean(x):
    return np.sum(x) / len(x)

def Median(x):
    N = len(x)
    sorted = np.sort(x)
    if N % 2 == 0:
        return (sorted[N/2] + sorted[1+N/2]) / 2.0
    else:
        return sorted[(N+1)/2]

def Std(x):
    mean = Mean(x)
    variance = np.sum((x - mean)**2) / len(x) - 1
    return np.sqrt(variance)

def Skew(x):
    N = len(x)
    mean = Mean(x)
    std = Std(x)
    sum = (x - mean) ** 3
    return sum / N*(std**3)

def Kurtosis(x):
    N = len(x)
    mean = Mean(x)
    std = Std(x)
    sum = (x - mean) ** 4
    return sum / N*(std**4) - 3.0


class KDE:
    def __init__(self, x, bandwidth):
        self.xvalues = x
        self.bw = bandwidth
        pass

    def value(self, x):
        sum = 0.0
        for xi in self.xvalues:
            sum += gaussian_kernel((x - xi) / self.bw)
        return sum / (len(self.xvalues) * self.bw)


def gaussian_kernel(u: float):
    return np.exp(-(u**2) / 2.0) / np.sqrt(2.0 * np.pi)
