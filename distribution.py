import pandas as pd
import numpy as np
import scipy.stats as sts
from utils import *
from my_statistics import Mean, Median, Std, Skew, Kurtosis


class Distribution:
    def __init__(self, data: pd.DataFrame):
        self.raw_data_ = data
        self.setup()
        pass

    def setup(self):
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
        df["cdf"] = df['rel-freq'].cumsum()

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

        functions = [
                     lambda data: np.std(data, ddof=1),
                     sts.skew, 
                     sts.kurtosis,
                     lambda data: 1.0 / np.sqrt(sts.kurtosis(data) + 3.0),
                    ]

        mean_l, mean_h, mean_std = mean_confidence_interval(self.raw_data_.iloc[:, 0], 0.05)
        info.loc['mean', 'CI-low'] = mean_l
        info.loc['mean', 'CI-high'] = mean_h
        info.loc['mean', 'std'] = mean_std
        median_l, median_h = median_confidence_interval(self.raw_data_.iloc[:, 0], 0.05)
        info.loc['median', 'CI-low'] = median_l
        info.loc['median', 'CI-high'] = median_h



        rows = ['std', 'skewness', 'kurtosis', 'antikurtosis']
        for i, row in enumerate(rows):
            l, h, std, _ = bootstrap(self.raw_data_.iloc[:, 0], functions[i], 1000, 0.05)
            info.loc[row, 'CI-low'] = l
            info.loc[row, 'CI-high'] = h
            info.loc[row, 'std'] = std

        


        info = info.T
        info.rename({0: "value"}, inplace=True)

        self.population_ = df
        self.population_info = info

    def get_classes_info(self, n: int = 0):
        if n == 0:
            n = calculate_classes_count(len(self.raw_data_))
        series = self.raw_data_.iloc[:, 0]
        hist, edges = np.histogram(
            series, n)
        classes_bounds = []
        prev = series.min()
        for edge in edges[1:]:
            classes_bounds.append([prev, edge])
            prev = edge
            pass

        classes = pd.DataFrame()
        classes['bounds'] = classes_bounds
        classes['freq'] = hist
        classes['rel-freq'] = hist / self.size()
        classes['ecdf'] = classes['rel-freq'].cumsum()
        return classes

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
        self.setup()
        pass

    def size(self):
        return len(self.raw_data_.index)

    def raw_x(self):
        return self.raw_data_[0].values

    def x(self):
        return self.population_['x'].values
    
    def cdf(self):
        return self.population_['cdf'].values

