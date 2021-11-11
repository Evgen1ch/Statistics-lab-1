import pandas as pd
import numpy as np
import scipy.stats as sts
from numpy import linalg


class Distribution:
    def __init__(self, data: pd.DataFrame):
        self.raw_data_ = data
        self.init_()
        pass

    def init_(self):
        # transforming dataframe into population
        data = self.raw_data_
        df = data[0]
        df = df.sort_values().reset_index(drop=True).value_counts()
        values = df.values
        sm = values.sum()

        df = pd.DataFrame(df)
        df["rel-freq"] = values / sm
        df = df.reset_index().rename(columns={'index': 'x', 0: 'freq'})
        df = df.sort_values(by='x').reset_index(drop=True)
        df["cumulative-probability"] = df['rel-freq'].cumsum()

        # collecting population statistics
        info = data.describe()
        median = data.median()

        # statistics 
        info = info.T
        info['median'] = median
        info['skewness'] = sts.skew(data.iloc[:, 0].values)
        info['kurtosis'] = sts.kurtosis(data.iloc[:, 0].values)
        info['antikurtosis'] = 1.0 / np.sqrt(info['kurtosis'].values[0] + 3)

        info = info[['count', 'mean', 'median', 'std', 'skewness', 'kurtosis', 'antikurtosis',
                     'min', 'max', '25%', '50%', '75%']]

        #statistics of statistics XD
        info = info.T
        info['std'] = 0
        info['CI-low'] = 0
        info['CI-high'] = 0

        functions = [np.mean,
                     np.median,
                     lambda data: np.std(data, ddof=1),
                     sts.skew, 
                     sts.kurtosis,
                     lambda data: 1.0 / np.sqrt(sts.kurtosis(data) + 3.0),
                    ]

        cols = ['mean', 'std', 'skewness', 'kurtosis', 'antikurtosis']
        for i, col in enumerate(cols):
            l, h, std, _ = bootstrap(self.raw_data_.iloc[:, 0], functions[i], 1000, 0.05)
            info.loc[col, 'CI-low'] = l
            info.loc[col, 'CI-high'] = h
            info.loc[col, 'std'] = std


        info = info.T
        info.rename({0: "value"}, inplace=True)

        series = data.iloc[:, 0]
        hist, edges = np.histogram(
            series, calculate_classes_count(self.size()))
        classes_bounds = []
        prev = series.min()
        for edge in edges[1:]:
            classes_bounds.append([prev, edge])
            prev = edge
            pass

        self.classes = pd.DataFrame()
        self.classes['bounds'] = classes_bounds
        self.classes['freq'] = hist
        self.classes['rel-freq'] = hist / self.size()
        self.classes['ecdf'] = self.classes['rel-freq'].cumsum()
        self.classes['ecdf'].values[-1] = 0.999999999999997

        self.population_ = df
        self.population_info = info

    def get_outliers_interval(self, k: float = 1.5) -> tuple[float, float]:
        q1: float = self.population_info['25%'].values[0]
        q3: float = self.population_info['75%'].values[0]

        a = q1 - k * (q3 - q1)
        b = q3 + k * (q3 - q1)
        return (a, b)

    def remove_outliers(self, k: float = 1.5):
        a, b = self.get_outliers_interval(k)

        self.raw_data_ = self.raw_data_[(self.raw_data_[0] > a)]
        self.raw_data_ = self.raw_data_[(self.raw_data_[0] < b)]
        self.init_()
        pass

    def size(self):
        return len(self.raw_data_)
    pass


def calculate_classes_count(n: int):
    return int(np.log10(n)*3.32 + 1)


def bootstrap(data, statistic, samples, error):
    results = []
    for i in range(samples):
        sample = np.random.choice(data, len(data), replace=True)
        results.append(statistic(sample))

    low = np.quantile(results, error/2.0)
    high = np.quantile(results, 1.0 - error/2.0)
    std = np.std(results)
    return low, high, std, results
