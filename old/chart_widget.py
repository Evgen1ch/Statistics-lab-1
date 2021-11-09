from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtCharts import *

import pandas as pd
import numpy as np
from population import Population


class ChartWidget:
    def __init__(self, widget, population: Population):
        super().__init__()
        self.widget = widget
        self.chart = QChart()
        self._chart_view = QChartView(self.chart)
        self._axis_y = QValueAxis()
        self._axis_x = QBarCategoryAxis()
        self._bar_series = QBarSeries()
        self._bar_series.setBarWidth(1.0)
        self.set = QBarSet("Dataset")

        self._population = population
        self._classes_count = 10

        # add new chart to parent widget
        self.widget.addWidget(self._chart_view)

    def add_chart(self):
        
        df = self._population.population_

        self._classes_count = 10#len(data) // 10

        # make_histogram
        min = df['X'].min()
        max = df["X"].max()
        h = (max - min) / self._classes_count

        classes = np.zeros(self._classes_count)

        for idx, vidx in enumerate(df.index[:-1]):
            row = df.loc[vidx]
            idx = int((row['X'] - min) / h)
            classes[idx] += row['freq']
        classes[-1]+=int(df.tail(1)['freq'])

        self.set.append(list(classes))
        self._bar_series.append(self.set)

        self.chart.addSeries(self._bar_series)

        # configuring axes
        self.chart.setAxisX(self._axis_x, self._bar_series)
        self.chart.setAxisY(self._axis_y, self._bar_series)
        self._axis_y.setRange(0, int(np.max(classes)*1.1))

        self.configure_chart_layout()

    def configure_chart_layout(self):
        # configuring legend
        self.chart.setTitle("Histogram")
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        # painting options
        self._chart_view.setRenderHint(QPainter.Antialiasing)
