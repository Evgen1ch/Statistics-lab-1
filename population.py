import pandas as pd


class Population:
    def __init__(self, data: pd.DataFrame):
        self.raw_data_ = data
        self.init_()
        pass

    def init_(self, data: pd.DataFrame):
        # dransforming dataframe into population
        df = data[0]
        df = df.sort_values().reset_index(drop=True).value_counts()
        values = df.values
        sm = values.sum()

        df = pd.DataFrame(df)
        df["rel. freq."] = values / sm
        df = df.reset_index().rename(columns={'index': 'X', 0: 'freq.'})

        # collecting population statistics
        info = data.describe()
        median = data.median()
        info = info.drop(['25%', '50%', '75%', 'count']).T
        info['median'] = median
        info = info.T

        self.population_ = df
        self.population_info = info
    pass
