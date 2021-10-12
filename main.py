

from typing import Mapping
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCharts import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 640, 400)
        self.setWindowTitle("hyello, world!")
        self.activate_()
    

    def activate(self):
        self.load_data()
        self.draw_line_chart()


    def load_data(self):
        pass

    def draw_line_chart(self):
        pass





if __name__ == "__main__":
    app = QApplication()
    win = Window()
    win.show()

    sys.exit(app.exec())


