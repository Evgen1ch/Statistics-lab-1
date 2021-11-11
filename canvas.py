import pandas as pd
import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from distribution import *

class MatplotlibHistCanvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(1, 1, dpi=150)
        self.ax2 = self.ax.twinx()
        super().__init__(figure=self.fig)
        self.setParent(parent)

    def set_data(self, data: pd.DataFrame, classes_count=0):
        if classes_count == 0:
            classes_count = calculate_classes_count(len(data.index))
        # plotting
        self.ax.clear()
        self.ax2.clear()

        self.data = data
        n, bins, patches = self.ax.hist(
            self.data, bins=classes_count, density=True)
        self.ax.set_xticks(bins)
        #self.ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: x / (len(data.index) * 1.0)))
        self.ax.set(xlabel='X', ylabel='count/size', title='Histogram')
        self.ax.axhline(y=0, color='k')
        self.ax.axvline(x=0, color='k')

        self.KDE()

        self.ax.grid()

        self.fig.canvas.draw_idle()

    def KDE(self):
        # calculate KDE using self.data
        series = self.data.iloc[:, 0]
        # min, max = self.ax.get_xlim()
        min, max = series.min(), series.max()
        x = np.linspace(min, max, 500)
        density = sts.kde.gaussian_kde(series, bw_method=0.5)
        y = density(x)
        self.ax2.plot(x, y, c='orange')
        self.ax2.set(ylabel='density')
        self.ax2.set_ylim(self.ax.get_ylim()[0], self.ax.get_ylim()[1])
        self.ax2.grid(color='lightgray', linestyle='--', alpha=0.5)
        pass

    # fix for
    # "ValueError: figure size must be positive finite not [ 0. -0.01333333]"
    #  on window creating
    def resizeEvent(self, event):
        if event.size().width() <= 0 or event.size().height() <= 0:
            return
        super(MatplotlibHistCanvas, self).resizeEvent(event)


class MatplotlibCDFCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(dpi=150)
        super().__init__(figure=self.fig)
        self.setParent(parent)

    def set_data(self, data: Distribution):
        self.ax.clear()
        #bins = len(data.index)

        df = data.population_
        df = df[['x', 'cumulative-probability']]
        for ri in df.index[:-1]:
            self.ax.plot(
                [df.loc[ri]['x'], df.loc[ri+1]['x']],
                [df.loc[ri]['cumulative-probability'],
                    df.loc[ri]['cumulative-probability']],
                linewidth=0.5, c='k'
            )

        #self.ax.hist(data, bins=bins, density=True, histtype='step', cumulative=True)

        self.ax.set(title="Cumulative distribution function",
                    xlabel='X', ylabel='F(X)')
        self.ax.axhline(y=0, color='k')
        self.ax.axvline(x=0, color='k')
        self.ax.grid()
        self.fig.canvas.draw_idle()
        pass


class MatplotlibOutliersCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(dpi=150)
        super().__init__(figure=self.fig)
        self.setParent(parent)

    def set_data(self, data: Distribution):
        self.ax.clear()

        df = data.raw_data_
        info = data.population_info

        k = np.array([1.5, 2, 2.5, 3])

        q1 = info['25%'].values[0]
        q3 = info['75%'].values[0]

        a = q1 - k * (q3 - q1)
        b = q3 + k * (q3 - q1)

        indices = df.index
        series = df.iloc[:, 0]

        self.ax.grid(color='lightgray', linewidth=0.5)
        self.ax.scatter(indices, series, c='#100057', s=3)
        colors = ['red', 'yellow', 'lightgreen', 'blue']
        for i in range(4):
            self.ax.axhline(y=a[i], c=colors[i], label="k={}".format(k[i]))
            self.ax.axhline(y=b[i], c=colors[i])
        self.ax.legend()
        self.fig.canvas.draw_idle()
        pass


class MatplotlibProbabilityPaperCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(dpi=150)
        super().__init__(figure=self.fig)
        self.setParent(parent)

    def set_data(self, data: Distribution):
        self.ax.clear()

        x = data.population_['x'].values[:-1]
        y = data.population_['cumulative-probability'].values[:-1]

        # symmetric log??????????
        pos: pd.Series = x[x >= 0]
        neg: pd.Series = x[x < 0]
        pos = np.log(pos)
        neg = -np.log(-neg)

        t = np.append(neg, pos)
        #t = np.log(x)
        z = np.log(-np.log(1 - y))

        self.ax.scatter(x=t, y=z, s=3, c='#100057')
        self.ax.set(xlabel='ln(x)', ylabel='ln(-ln(1-F(x)))',
                    title="Probability paper")
        self.ax.grid()

        lx = t
        ly = z
        meanx = lx.mean()
        meany = ly.mean()

        numer = (lx - meanx) * (ly - meany)
        denom = (lx - meanx) ** 2
        numer = numer.sum()
        denom = denom.sum()
        a = numer / denom
        b = meany - (meanx * a)

        linx = np.array([lx.min(), lx.max()])
        liny = linx * a + b
        self.ax.plot(linx, liny, c='red')

        self.fig.canvas.draw_idle()
        pass