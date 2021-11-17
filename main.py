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
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.configure_tabs()
        self.configure_events()

        self.load_dummy()

        self.showMaximized()

    def init_to_data(self):
        
        c = calculate_classes_count(
            len(self.distribution.raw_data_.index))
        bw = calculate_bandwidth(self.distribution.raw_x())
        k = 1.5

        # charts
        self.initCdf()
        self.histCanvas.clear()
        self.histCanvas.set_data(self.distribution.raw_x(), c, bw)
        self.initPaper()
        self.outliersCanvas.set_data(self.distribution.raw_x())
        self.outliersCanvas.draw_lines(*self.distribution.get_outliers_interval(k))

        #tables
        self.fill_table(self.tableWidget, self.distribution.population_)
        self.updateClassTable(c)
        self.set_population_info()

        self.init_ui_to_data(c, bw, k)

    def init_ui_to_data(self, c, bw, k):
        self.kSpinBox.setValue(k)
        # set interval for detecting outliers
        self.intervalValLabel.setText("[{0}, {1}]".format(
            *self.distribution.get_outliers_interval(k)))
        
        self.aLineEdit.setText("")
        self.bLineEdit.setText("")

        self.histClassesSpinBox.setValue(c)
        self.kdeBandwidthSpinBox.setValue(bw)

        self.chiSquareLineEdit.setText("")
        self.critChiSquareLineEdit.setText("")
        self.confidenceIntervallForALineEdit.setText("")
        self.confidenceIntervalForBLineEdit.setText("")
        self.isDistrubutionProbableLineEdit.setText("")
        self.aLineEdit_2.setText("")
        self.bLineEdit_2.setText("")
        self.pValueLineEdit.setText("")
        self.aStdLineEdit.setText("")
        self.bStdLineEdit.setText("")

    def initCdf(self):
        x = self.distribution.x()
        y = self.distribution.cdf()
        self.ecdfCanvas.draw_cdf(x, y)
        pass

    def updateHistKde(self):
        classesSB: QSpinBox = self.histClassesSpinBox
        c = classesSB.value()
        bwsb: QSpinBox = self.kdeBandwidthSpinBox
        bw = bwsb.value()
        x = self.distribution.raw_x()
        self.histCanvas.set_data(x, c, bw)
        self.updateClassTable(c)
        pass

    def initPaper(self):
        self.paperCanvas.clear()
        x = self.distribution.x()[:-1]
        y = self.distribution.cdf()[:-1]

        if len(x[x < 0.0]) > 0:
            self.probPaperInfo.setText("Info: Can not convert negative values")
            return

        t, z = calculate_paper_axes(x, y)
        self.paperCanvas.draw_data(t, z)
        self.probPaperInfo.setText("")
        pass

    def updateOutliers(self):
        sb: QDoubleSpinBox = self.kSpinBox
        K = sb.value()
        a, b = self.distribution.get_outliers_interval(k=K)
        x = self.distribution.raw_x()
        self.outliersCanvas.draw_lines(a, b)
        # set interval for detecting outliers
        self.intervalValLabel.setText("[{0}, {1}]".format(a, b))

    def updateClassTable(self, classes=0):
        self.fill_table(self.densityClassInfoTableWidget,
                        self.distribution.get_classes_info(classes))
        header: QHeaderView = self.densityClassInfoTableWidget.horizontalHeader()
        header.setSectionResizeMode(0,QHeaderView.ResizeToContents)
        pass

    def load_data(self, filename: str):
        dataframe: pd.DataFrame = pd.read_csv(filename, header=None)
        if object in dataframe.dtypes:
            msg = QMessageBox(icon=QMessageBox.Critical, title='Bad file')
            msg.setText(
                "File must only contain numeric data. Maybbe your data not comma separated.")
            msg.exec()
            return
        self.distribution = Distribution(dataframe)
        self.init_to_data()

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
        df = self.distribution.population_info.T
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

    def on_input_file_button_cliked(self):
        filename, filter = QFileDialog.getOpenFileName(
            parent=self, caption='Open file', directory='.')
        if os.path.exists(filename) and os.path.isfile(filename):
            self.filenameLineEdit.setText(filename)
            self.load_data(filename)

    def on_load_file_button_clicked(self):
        edit: QLineEdit = self.filenameLineEdit
        filename = edit.text()
        if os.path.exists(filename) and os.path.isfile(filename):
            self.load_data(filename)

    def on_restore_cdf_button_clicked(self):
        x = self.distribution.x()
        y = self.distribution.cdf()
        if len(x[x < 0.0]) > 0:
            msg = QMessageBox(icon=QMessageBox.Information,
                              text='Weibull distribution can not contain negative values')
            msg.exec()
            return

        a, b, cia, cib, stda, stdb = restore_veibull_distribution(x[:-1], y[:-1], 0.05)
        yi = weib(x, a, b)

        # drawing restored cdf
        self.ecdfCanvas.draw_restored_cdf(x, yi)

        #drawing restored pdf
        self.histCanvas.draw_restored_pdf(x, a, b)

        # drawing probability paper plot approximation line
        t = np.array([np.min(x), np.max(x[:-1])])
        z = np.array([np.min(y), np.max(y[:-1])])
        t, z = calculate_paper_axes(t, z)
        loga = -np.log(a)
        z = t*b + loga
        self.paperCanvas.draw_line(t, z)

        # calculating chi squared
        x = self.distribution.raw_x()
        is_true, chi2, crit, p = chi_square_test(
            x, a, b, 0.05, calculate_classes_count(self.distribution.size()))

        # updating intarface
        self.confidenceIntervallForALineEdit.setText(
            "[{0}, {1}]".format(cia[0], cia[1]))
        self.confidenceIntervalForBLineEdit.setText(
            "[{0}, {1}]".format(cib[0], cib[1]))
        self.chiSquareLineEdit.setText(str(chi2))
        self.critChiSquareLineEdit.setText(str(crit))
        self.isDistrubutionProbableLineEdit.setText(str(is_true))
        self.aLineEdit_2.setText(str(a))
        self.bLineEdit_2.setText(str(b))
        self.aStdLineEdit.setText(str(stda))
        self.bStdLineEdit.setText(str(stdb))
        self.pValueLineEdit.setText(str(p))

        self.aLineEdit.setText(str(loga))
        self.bLineEdit.setText(str(b))
        pass

    def on_remove_outliers_button_clicked(self):
        sb: QDoubleSpinBox = self.kSpinBox
        K = sb.value()
        self.distribution.remove_outliers(k=K)
        self.init_to_data()
        pass

    def on_update_kde_button_clicked(self):
        self.updateHistKde()
        pass

    def on_update_k_button_clicked(self):
        self.updateOutliers()
        pass

    def configure_events(self):
        filenameBtn: QPushButton = self.filenamePushButton
        filenameBtn.clicked.connect(self.on_input_file_button_cliked)

        filenameLoadBtn: QPushButton = self.pushButton
        filenameLoadBtn.clicked.connect(self.on_load_file_button_clicked)

        removeBtn: QPushButton = self.removeOutliersPushButton
        removeBtn.clicked.connect(self.on_remove_outliers_button_clicked)

        restoreBtn: QPushButton = self.restoreCumulativePushButton
        restoreBtn.clicked.connect(self.on_restore_cdf_button_clicked)

        updateKdeBtn: QPushButton = self.updateHistKdePushButton
        updateKdeBtn.clicked.connect(self.on_update_kde_button_clicked)

        changeKBtn: QPushButton = self.updateKPushButton
        changeKBtn.clicked.connect(self.on_update_k_button_clicked)
        pass

    def configure_tabs(self):
        # configuring histogram tab
        self.histCanvas = MatplotlibHistKDECanvas(self)
        self.toolbarHist = NavigationToolbar(self.histCanvas, self)
        densityTab: QVBoxLayout = self.densityPlotVerticalLayout
        densityTab.addWidget(self.toolbarHist)
        densityTab.addWidget(self.histCanvas)

        # configuring ecdf tab
        self.ecdfCanvas = MatplotlibCDFCanvas(self)
        self.toolBarEcdf = NavigationToolbar(self.ecdfCanvas, self)
        esdfTab: QVBoxLayout = self.ecdfVerticalLayout
        esdfTab.addWidget(self.toolBarEcdf)
        esdfTab.addWidget(self.ecdfCanvas)

        # configuring paper tab
        self.paperCanvas = MatplotlibProbabilityPaperCanvas(self)
        self.toolBarPaper = NavigationToolbar(self.paperCanvas, self)
        densityTab: QVBoxLayout = self.paperPlotVerticalLayout
        densityTab.addWidget(self.toolBarPaper)
        densityTab.addWidget(self.paperCanvas)

        # configuring outliers tab
        self.outliersCanvas = MatplotlibOutliersCanvas(self)
        self.toolbarOutliers = NavigationToolbar(self.outliersCanvas, self)
        outliersTab: QVBoxLayout = self.outliersPlotVerticalLayout
        outliersTab.addWidget(self.toolbarOutliers)
        outliersTab.addWidget(self.outliersCanvas)
        pass

    def load_dummy(self):
        self.distribution = Distribution(pd.DataFrame(
            np.random.normal(size=100, loc=0, scale=2)))
        self.init_to_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = AppWindow()
    wnd.show()
    sys.exit(app.exec())
