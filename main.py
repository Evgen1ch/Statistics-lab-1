import pandas as pd
import sys

from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import pandas as pd

from chart_widget import ChartWidget

ui, _ = loadUiType("style/test.ui")


class Window(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("hyello, world!")
        self.activate_()

    def activate_(self):
        self.load_data()
        self.draw_line_chart()

    def load_data(self):
        df = pd.read_csv('data_lab1/70/norm.txt', header=None)
        # generating names for colmns that looks like x1, x2, x3, etc.
        self._data = df
        self._series = df.transpose()[0]
        names = []
        for i in range(0, len(df.columns)):
            names.append('x' + str(i + 1))
        df.columns = names

        table = self.tableWidget
        table.setStyleSheet("background-color: #dddddd; color: #111111")
        table.setColumnCount(len(df.columns))
        table.setHorizontalHeaderLabels(df.columns)
        table.setRowCount(len(df.index))

        header = table.horizontalHeader()
        header.setStyleSheet("background-color: #dddddd; color: #111111")

        for rn, row in enumerate(df.index):
            for cn, col in enumerate(df.columns):
                item = QTableWidgetItem(str(df.loc[row, col]))
                table.setItem(rn, cn, item)
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        
        pass

    def draw_line_chart(self):
        wid = self.plotLayout
        cw = ChartWidget(wid, self._data)
        cw.add_chart()
        pass


if __name__ == "__main__":
    app = QApplication()
    win = Window()
    win.show()

    sys.exit(app.exec())
