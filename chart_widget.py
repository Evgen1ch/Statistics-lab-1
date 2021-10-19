from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QPainter
from PySide6.QtCharts import *

import pandas as pd
import numpy as np


class ChartWidget:
    def __init__(self, widget, data):
        super().__init__()
        self.widget = widget
        self.chart = QChart()
        self._chart_view = QChartView(self.chart)
        self._axis_y = QValueAxis()
        self._axis_x = QBarCategoryAxis()
        self._bar_series = QBarSeries()

        self._data = data
        self._classes_count = 10
        
        self._bar_series = QBarSeries()
        self.set0 = QBarSet("Dataset")

    def add_chart(self):
        data = pd.DataFrame(self._data)
        data = data.iloc[:, 0].to_list()

        # make_histogram
        min = np.min(data)
        max = np.max(data)
        step = (max - min) / self._classes_count

        classes = np.zeros(self._classes_count + 1)

        for x in data:
            idx = int((x - min) / step)
            classes[idx]+=1
            pass
        
        a = self._data[self._data < min + step].dropna()
        print(a)
        
        self.set0.append(list(classes))
        self._bar_series.append(self.set0)

        self.chart.addSeries(self._bar_series)
        self._bar_series.setBarWidth(1.0)

        # configuring axes
        self.chart.setAxisX(self._axis_x, self._bar_series)

        self.chart.setAxisY(self._axis_y, self._bar_series)
        self._axis_y.setRange(0, int(np.max(classes)*1.1))

        # configuring legend
        self.chart.setTitle("Histogram")
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        # painting options
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.widget.addWidget(self._chart_view)
