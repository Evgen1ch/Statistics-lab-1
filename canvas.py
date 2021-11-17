import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from distribution import calculate_classes_count
from weibull import weib_density

from my_statistics import *

class MatplotlibCDFCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(dpi=150)
        super().__init__(figure=self.fig)
        self.setParent(parent)

    def draw_cdf(self, x, y):
        self.ax.clear()
        for i in range(len(x) - 1):
            self.ax.plot([x[i], x[i+1]], [y[i], y[i]], linewidth=0.6, c='k')
        self.ax.axhline(y=0, color='k')
        self.ax.axvline(x=0, color='k')
        self.ax.grid()
        self.ax.set(title='Cumulative distribution function', xlabel='X', ylabel='F(X)')
        self.fig.canvas.draw_idle()

    def draw_restored_cdf(self, x, y):
        # self.ax.clear()
        self.ax.plot(x, y, c='orange')
        self.fig.canvas.draw_idle()

class MatplotlibHistKDECanvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(1, 1, dpi=150)
        self.a, self.b = None, None
        super().__init__(figure=self.fig)
        self.setParent(parent)
     
    def set_data(self, data, classes_count=0, bw=0.5):
        if classes_count == 0:
            classes_count = calculate_classes_count(len(data))
        self.ax.clear()
        #HIST
        n, bins, patches = self.ax.hist(
            data, bins=classes_count, density=True)
        self.ax.set_xticks(bins)
        self.ax.axhline(y=0, color='k')
        self.ax.axvline(x=0, color='k')
        #KDE
        min, max = np.min(data), np.max(data)
        x = np.linspace(min, max, 500)
        kde = KDE(data, bw)
        y = [kde.value(xi) for xi in x]
        self.ax.plot(x, y, c='lightgreen', label="KDE")
        self.ax.grid()
        self.ax.set(xlabel='X', ylabel='density', title='Histogram and KDE')
        if self.a != None and self.b != None:
            self.draw_restored_pdf(x, self.a, self.b)
        self.ax.legend()
        self.fig.canvas.draw_idle()

    def draw_restored_pdf(self, x, a, b):
        self.a = a
        self.b = b
        y = weib_density(x, a, b)
        self.ax.plot(x, y, c='orange', label='Restored PDF')
        self.ax.legend()
        self.fig.canvas.draw_idle()
        pass

    def clear(self):
        self.ax.clear()
        self.a, self.b = None, None

    def resizeEvent(self, event):
        # fix for
        # "ValueError: figure size must be positive finite not [ 0. -0.01333333]"
        #  on window creating
        if event.size().width() <= 0 or event.size().height() <= 0:
            return
        super(MatplotlibHistKDECanvas, self).resizeEvent(event)

class MatplotlibProbabilityPaperCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(dpi=150)
        super().__init__(figure=self.fig)
        self.setParent(parent)

    def draw_data(self, t, z):
        self.ax.scatter(x=t, y=z,s=3,c="#100057")
        self.ax.set(xlabel='ln(x)', ylabel='ln(-ln(1-F(x)))', title='Probability paper')
        self.ax.grid()
        self.fig.canvas.draw_idle()
        pass

    def draw_line(self, x, y):
        self.ax.plot(x,y,c='orange')
        self.fig.canvas.draw_idle()
        pass

    def clear(self):
        self.ax.clear()

class MatplotlibOutliersCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(dpi=150)
        super().__init__(figure=self.fig)
        self.setParent(parent)

    def set_data(self, x):
        self.ax.clear()
        indices = np.arange(len(x))
        series = x
        self.ax.grid(color='lightgray', linewidth=0.5)
        self.ax.scatter(indices, series, c='#100057', s=3)
        self.fig.canvas.draw_idle()
    
    def draw_lines(self, a:float, b:float):
        if len(self.ax.lines) >= 1:
            self.ax.lines.pop(0)
            self.ax.lines.pop(0)
        self.ax.axhline(y=a, c='red')
        self.ax.axhline(y=b, c='red')
        self.fig.canvas.draw_idle()
        pass
