from population import Population, calculate_classes_count
from style.UIClass import Ui_MainWindow

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys
import os

import numpy as np
import pandas as pd
import scipy.stats as sts

import timeit
import time

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
matplotlib.use("Qt5Agg")


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

    def set_data(self, data: Population):
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

    def set_data(self, data: Population):
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

    def set_data(self, data: Population):

        self.ax.clear()

        x = data.population_['x']
        y = data.population_['cumulative-probability']
        # subtract very little value from last cumulative function value because of value in 1.0 is infinity
        if (y.values[-1] >= 1.0):
            y.values[-1] -= 1e-15

        # symmetric log??????????
        pos: pd.Series = x[x >= 0]
        neg: pd.Series = x[x < 0]
        pos = np.log(pos)
        neg = -np.log(-neg)

        t = neg.append(pos)
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


class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.configure_tabs()
        self.configure_events()

        self.showMaximized()

    def update_charts(self):
        # charts
        classes_count = calculate_classes_count(
            len(self.population.raw_data_.index))
        self.histCanvas.set_data(self.population.raw_data_, classes_count)
        self.ecdfCanvas.set_data(self.population)
        self.paperCanvas.set_data(self.population)
        self.outliersCanvas.set_data(self.population)

        #refill tables
        self.fill_table(self.tableWidget, self.population.population_)
        self.fill_table(self.densityClassInfoTableWidget,
                        self.population.classes)
        self.set_population_info()

        # set interval for detecting outliers
        self.intervalValLabel.setText("[{0}, {1}]".format(
            *self.population.get_outliers_interval()))
        pass

    def load_data(self, filename: str):
        dataframe = pd.read_csv(filename, header=None)
        self.population = Population(dataframe)
        # start = time.time()
        # self.fill_table(self.tableWidget, self.population.population_)
        # end = time.time()
        # print("[INFO] Population table loaded. Estimated time:", end - start)

        # start = time.time()
        # self.fill_table(self.densityClassInfoTableWidget,
        #                 self.population.classes)
        # end = time.time()
        # print("[INFO] Classes table loaded. Estimated time:", end - start)

    def format_entry(self, entry):
        if np.isscalar(entry):
            return "{0:.9f}".format(entry)
        elif isinstance(entry, list):
            copy = entry.copy()
            for i in range(0, len(entry)):
                copy[i] = "{0:.9f}".format(entry[i])
            return str(copy).replace("'", '')

    def fill_table(self, table: QTableWidget, df: pd.DataFrame):
        table.clear()
        # reset appearence of table
        self.configure_table_appearence(table, df)
        for rn, row in enumerate(df.index):
            for cn, col in enumerate(df.columns):
                item = QTableWidgetItem(self.format_entry(df.loc[row, col]))
                table.setItem(rn, cn, item)
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def set_population_info(self):
        info = self.population.population_info
        count: QLabel = self.countValLabel
        min: QLabel = self.minValLabel
        max: QLabel = self.maxValLabel
        mean: QLabel = self.meanValLabel
        median: QLabel = self.medianValLabel
        std: QLabel = self.stdValLabel
        skewness: QLabel = self.skewnessValLabel
        kurtosis: QLabel = self.kurtosisValLabel
        antikurtosis: QLabel = self.antikurtosisValLabel

        count.setText(str(info['count'].values[0]))
        min.setText(str(info['min'].values[0]))
        max.setText(str(info['max'].values[0]))
        mean.setText(str(info['mean'].values[0]))
        median.setText(str(info['median'].values[0]))
        std.setText(str(info['std'].values[0]))
        skewness.setText(str(info['skewness'].values[0]))
        kurtosis.setText(str(info['kurtosis'].values[0]))
        antikurtosis.setText(str(info['antikurtosis'].values[0]))
        pass

    def configure_table_appearence(self, table: QTableWidget, df: pd.DataFrame):
        table.setColumnCount(len(df.columns))
        table.setHorizontalHeaderLabels(df.columns)
        table.setRowCount(len(df.index))
        table.setStyleSheet("background-color: #dddddd; color: #111111")
        table.horizontalHeader().setStyleSheet(
            "background-color: #dddddd; color: #111111")
        # header = table.horizontalHeader()
        # next three limes make table loading very slow
        # table.horizontalHeader().setStretchLastSection(True)
        # header.setSectionResizeMode(QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(0, QHeaderView.Stretch)

    def on_input_file_button_cliked(self):
        filename, filter = QFileDialog.getOpenFileName(
            parent=self, caption='Open file', directory='.')
        if os.path.exists(filename) and os.path.isfile(filename):
            textEdit: QTextEdit = self.filenameLineEdit
            textEdit.setText(filename)

            self.load_data(filename)
            self.update_charts()
            self.set_population_info()

    def on_restore_ecdf_button_clicked(self):
        # todo
        pass

    def on_remove_outliers_button_clicked(self):
        self.population.remove_outliers()
        self.update_charts()
        pass

    def configure_events(self):
        filenameBtn: QPushButton = self.filenamePushButton
        filenameBtn.clicked.connect(self.on_input_file_button_cliked)

        removeBtn: QPushButton = self.removeOutliersPushButton
        removeBtn.clicked.connect(self.on_remove_outliers_button_clicked)

        restoreBtn: QPushButton = self.restoreCumulativePushButton
        restoreBtn.clicked.connect(self.on_restore_ecdf_button_clicked)
        pass

    def configure_tabs(self):
        self.histCanvas = MatplotlibHistCanvas(self)
        self.ecdfCanvas = MatplotlibCDFCanvas(self)
        self.paperCanvas = MatplotlibProbabilityPaperCanvas(self)
        self.outliersCanvas = MatplotlibOutliersCanvas(self)
        self.toolbarHist = NavigationToolbar(self.histCanvas, self)
        self.toolBarEcdf = NavigationToolbar(self.ecdfCanvas, self)
        self.toolBarPaper = NavigationToolbar(self.paperCanvas, self)
        self.toolbarOutliers = NavigationToolbar(self.outliersCanvas, self)

        self.population = Population(pd.DataFrame(
            np.random.normal(size=100, loc=0, scale=2)))
        self.histCanvas.set_data(
            self.population.raw_data_, calculate_classes_count(1000))
        self.ecdfCanvas.set_data(self.population)
        self.paperCanvas.set_data(self.population)
        self.outliersCanvas.set_data(self.population)
        self.fill_table(self.tableWidget, self.population.population_)

        # configuring histogram tab
        densityTab: QVBoxLayout = self.densityPlotVerticalLayout
        densityTab.addWidget(self.toolbarHist)
        densityTab.addWidget(self.histCanvas)

        # configuring ecdf tab
        esdfTab: QVBoxLayout = self.ecdfVerticalLayout
        esdfTab.addWidget(self.toolBarEcdf)
        esdfTab.addWidget(self.ecdfCanvas)

        # configuring paper tab
        densityTab: QVBoxLayout = self.paperPlotVerticalLayout
        densityTab.addWidget(self.toolBarPaper)
        densityTab.addWidget(self.paperCanvas)

        # configuring outliers tab
        outliersTab: QVBoxLayout = self.outliersPlotVerticalLayout
        outliersTab.addWidget(self.toolbarOutliers)
        outliersTab.addWidget(self.outliersCanvas)
        pass


if __name__ == "__main__":
    # population = Population(pd.DataFrame(np.random.normal(size=1000, loc=0, scale=1)))
    # population.raw_data_.plot(kind='density')
    # error = 0.05
    # n = population.size() * 1.0
    # degrees_freedom = n - 1
    # confidence_level = 1.0 - error/2.0
    
    # error = 0.05
    # print(sts.norm.ppf(0.975))
    # print(sts.t.ppf(0.975, df=100))
    # print(sts.pearson3.ppf(0.975, skew=100))
    

    # res = sts.bootstrap((population.raw_data_,), np.std, method='percentile', confidence_level=confidence_level)
    # print(res.confidence_interval)
    # plt.axvline(x=res.confidence_interval.low)
    # plt.axvline(x=res.confidence_interval.high)
    # plt.show()

    # std_std = population.raw_data_.std() / np.sqrt(2.0*n)
    # interval = sts.t.interval(alpha=confidence_level, df=degrees_freedom, loc=population.raw_data_.std(), scale=std_std)
    # print(interval)

    
    # j = n / 2.0 - (sts.norm.ppf(confidence_level) * np.sqrt(n) / 2.0)
    # k = n / 2.0 + (sts.norm.ppf(confidence_level) * np.sqrt(n) / 2.0)
    # print(j, k)




    app = QApplication(sys.argv)
    wnd = AppWindow()
    wnd.show()
    sys.exit(app.exec())
