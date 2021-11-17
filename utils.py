import numpy as np
import scipy.stats as sts
import statistics as stats
def calculate_classes_count(n: int):
    return int(np.log10(n)*3.32 + 1)

def calculate_bandwidth(x):
    print(np.std(x, ddof=1), len(x))
    return np.std(x, ddof=1) / (len(x) ** 0.2)
   

def bootstrap(data, statistic, samples, error):
    results = []
    for i in range(samples):
        sample = np.random.choice(data, len(data), replace=True)
        results.append(statistic(sample))
    
    results = np.sort(results)
    low = np.quantile(results, error/2.0)
    high = np.quantile(results, 1.0 - error/2.0)
    std = np.std(results, ddof=1)
    return low, high, std, results

def mean_confidence_interval(x, error):
    t = sts.t.ppf(1.0 - error/2.0, len(x) - 1)
    mean = np.mean(x)
    mean_std = np.std(x, ddof=1) / np.sqrt(len(x))
    meanl = mean - t * mean_std
    meanh = mean + t * mean_std
    return (meanl, meanh, mean_std)

def median_confidence_interval(x, error):
    N = len(x)
    u = sts.norm.ppf(1.0-error/2.0)
    j = int(N/2.0 - u * np.sqrt(N)/2.0)
    k = int(N/2.0 + u * np.sqrt(N)/2.0)
    t = np.sort(x)
    return (t[j], t[k])



