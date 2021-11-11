from distribution import *
from style.UIClass import Ui_MainWindow
from canvas import *
from weibull import *

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys
import os

import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.configure_tabs()
        self.configure_events()

        self.showMaximized()

    def update(self):
        # charts
        classes_count = calculate_classes_count(
            len(self.population.raw_data_.index))
        self.histCanvas.set_data(self.population.raw_data_, classes_count)
        self.ecdfCanvas.set_data(self.population)
        self.paperCanvas.set_data(self.population)
        self.outliersCanvas.set_data(self.population)

        # refill tables
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
        self.population = Distribution(dataframe)

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
        df = self.population.population_info.T
        table: QTableWidget = self.distributionStatisticsTableWidget
        table.clear()

        cols = ['statistic']+(list(map(str, df.columns)))
        table.setColumnCount(len(df.columns) + 1)
        table.setRowCount(len(df.index))
        table.setHorizontalHeaderLabels(cols)
        table.setStyleSheet("background-color: #dddddd; color: #111111")
        table.horizontalHeader().setStyleSheet(
            "background-color: #dddddd; color: #111111")

        for rn, row in enumerate(df.index):
            table.setItem(rn, 0, QTableWidgetItem(row))
            for cn, col in enumerate(df.columns):
                item = QTableWidgetItem(self.format_entry(df.loc[row, col]))
                table.setItem(rn, cn + 1, item)
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        pass

    def configure_table_appearence(self, table: QTableWidget, df: pd.DataFrame):
        table.setColumnCount(len(df.columns))
        table.setHorizontalHeaderLabels(map(str, df.columns))
        table.setRowCount(len(df.index))
        table.setStyleSheet("background-color: #dddddd; color: #111111")
        table.horizontalHeader().setStyleSheet(
            "background-color: #dddddd; color: #111111")
        header = table.horizontalHeader()
        #header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
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
            self.update()

    def on_load_file_button_clicked(self):
        edit: QLineEdit = self.filenameLineEdit
        filename = edit.text()
        if os.path.exists(filename) and os.path.isfile(filename):
            self.load_data(filename)
            self.update()

    def on_restore_ecdf_button_clicked(self):
        # todo min squares things
        pass

    def on_remove_outliers_button_clicked(self):
        self.population.remove_outliers()
        self.update()
        pass

    def configure_events(self):
        filenameBtn: QPushButton = self.filenamePushButton
        filenameBtn.clicked.connect(self.on_input_file_button_cliked)

        filenameLoadBtn: QPushButton = self.pushButton
        filenameLoadBtn.clicked.connect(self.on_load_file_button_clicked)

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

        self.population = Distribution(pd.DataFrame(
            np.random.normal(size=100, loc=0, scale=2)))
        self.update()

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
    # app = QApplication(sys.argv)
    # wnd = AppWindow()
    # wnd.show()
    # sys.exit(app.exec())

    d = Distribution(pd.read_csv("data_lab1/500/exp.txt", header=None))
    x = d.population_['x']
    y = d.population_['cumulative-probability']

    a, b, cia, cib, = restore_veibull_distribution(x[:-1], y[:-1])
    print(a, b)

    xi = np.linspace(x.min(), x.max(), 1000)
    ci = weib(x, a, b)
    dens = weib_density(x, a, b)

    plt.figure(figsize=(10, 10), dpi=150)

    plt.plot(x, ci, c='orange',
             label='restored 1.0 - exp(-x^b/a)\na = {0}\nb = {1}'.format(a, b))

    plt.scatter(x, y, s=3)
    plt.legend()

    fig, ax = plt.subplots(dpi=150)
    ax.plot(x, dens, c='green')
    x.plot(kind='density', bw_method=.25)
    ax.hist(x, density=True, alpha=0.5)
    plt.show()

    x = d.population_['x'].values
    probable, chi2, crit = chi_square_test(x, a, b, 0.05, 200)
    print(probable, chi2, crit)
