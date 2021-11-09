import pandas as pd
import sys
import os

from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import pandas as pd

from chart_widget import ChartWidget
from population import Population
from population import calculate_classes_count

ui, _ = loadUiType("style/test.ui")


class Window(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("hyello, world!")

        self.configure_events()

    def configure_events(self):
        fileSelectButton: QPushButton = self.selectFileButton
        fileSelectButton.clicked.connect(self.onInputFileButtonClicked)

    def load_data(self, filename):
        df = pd.read_csv(filename, header=None)

        self.population = Population(df)

        self.configure_table()
        self.fill_table()

    def configure_table(self):
        df = self.population.population_
        table: QTableWidget = self.tableWidget
        table.setStyleSheet("background-color: #dddddd; color: #111111")
        table.setColumnCount(len(df.columns))
        table.setHorizontalHeaderLabels(df.columns)
        table.setRowCount(len(df.index))
        header = table.horizontalHeader()
        header.setStyleSheet("background-color: #dddddd; color: #111111")

    def fill_table(self):
        df = self.population.population_
        table: QTableWidget = self.tableWidget
        # fill table with data
        for rn, row in enumerate(df.index):
            for cn, col in enumerate(df.columns):
                item = QTableWidgetItem("{0:.9f}".format(df.loc[row, col]))
                table.setItem(rn, cn, item)
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def onInputFileButtonClicked(self):
        filename, filter = QFileDialog.getOpenFileName(
            parent=self, caption='Open file', dir='.')
        if os.path.exists(filename) and os.path.isfile(filename):
            text_edit: QTextEdit = self.textEditFilename
            text_edit.setText(filename)
            self.load_data(filename)
            self.draw_histogram()

    def draw_histogram(self):
        wid: QVBoxLayout = self.plotLayout
        # remove previous output
        prev = wid.takeAt(0)
        if not prev == None:
            wid.removeItem(prev)

        # create new widget with new chart
        cw = ChartWidget(wid, self.population)
        cw.add_chart()


if __name__ == "__main__":
    app = QApplication()
    win = Window()
    win.show()

    sys.exit(app.exec())
