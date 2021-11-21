import numpy as np
import scipy.stats as sts
from my_statistics import *
def calculate_classes_count(n: int):
    return int(np.log10(n)*3.32 + 1)

def calculate_bandwidth(x):
    return Std(x) / (len(x) ** 0.2)

def bootstrap(data, statistic, samples, error):
    results = []
    for i in range(samples):
        sample = np.random.choice(data, len(data), replace=True)
        results.append(statistic(sample))
    
    results = np.sort(results)
    low = np.quantile(results, error/2.0)
    high = np.quantile(results, 1.0 - error/2.0)
    std = Std(results)
    return low, high, std, results

def make_histogram(x, classes: int, density: bool = False):
    min = np.min(x)
    max = np.max(x)
    h = (max - min) / classes

    edges = []
    for i in range(classes + 1):
        edges.append(min + i * h)

    bins = np.zeros(classes, dtype=np.int32)
    for xi in x:
        idx = int((xi - min)/ h)
        if idx == classes:
            bins[-1]+=1
        else:
            bins[idx]+=1
    
    if density:
        bins = bins / (len(x) * h)

    return bins, edges



