# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.rootLayout = QVBoxLayout()
        self.rootLayout.setObjectName(u"rootLayout")
        self.mainHorizontalLayout = QHBoxLayout()
        self.mainHorizontalLayout.setObjectName(u"mainHorizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inputFilenameLayout = QHBoxLayout()
        self.inputFilenameLayout.setObjectName(u"inputFilenameLayout")
        self.filenameLineEdit = QLineEdit(self.centralwidget)
        self.filenameLineEdit.setObjectName(u"filenameLineEdit")

        self.inputFilenameLayout.addWidget(self.filenameLineEdit)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.inputFilenameLayout.addWidget(self.pushButton)

        self.filenamePushButton = QPushButton(self.centralwidget)
        self.filenamePushButton.setObjectName(u"filenamePushButton")

        self.inputFilenameLayout.addWidget(self.filenamePushButton)


        self.verticalLayout.addLayout(self.inputFilenameLayout)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(20)
        self.countLabel = QLabel(self.centralwidget)
        self.countLabel.setObjectName(u"countLabel")
        font = QFont()
        font.setPointSize(10)
        self.countLabel.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.countLabel)

        self.countValLabel = QLabel(self.centralwidget)
        self.countValLabel.setObjectName(u"countValLabel")
        self.countValLabel.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.countValLabel)

        self.meanLabel = QLabel(self.centralwidget)
        self.meanLabel.setObjectName(u"meanLabel")
        self.meanLabel.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.meanLabel)

        self.meanValLabel = QLabel(self.centralwidget)
        self.meanValLabel.setObjectName(u"meanValLabel")
        self.meanValLabel.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.meanValLabel)

        self.medianLabel = QLabel(self.centralwidget)
        self.medianLabel.setObjectName(u"medianLabel")
        self.medianLabel.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.medianLabel)

        self.medianValLabel = QLabel(self.centralwidget)
        self.medianValLabel.setObjectName(u"medianValLabel")
        self.medianValLabel.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.medianValLabel)

        self.stdLabel = QLabel(self.centralwidget)
        self.stdLabel.setObjectName(u"stdLabel")
        self.stdLabel.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.stdLabel)

        self.stdValLabel = QLabel(self.centralwidget)
        self.stdValLabel.setObjectName(u"stdValLabel")
        self.stdValLabel.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.stdValLabel)

        self.skewnessLabel = QLabel(self.centralwidget)
        self.skewnessLabel.setObjectName(u"skewnessLabel")
        self.skewnessLabel.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.skewnessLabel)

        self.skewnessValLabel = QLabel(self.centralwidget)
        self.skewnessValLabel.setObjectName(u"skewnessValLabel")
        self.skewnessValLabel.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.skewnessValLabel)

        self.kurtosisLabel = QLabel(self.centralwidget)
        self.kurtosisLabel.setObjectName(u"kurtosisLabel")
        self.kurtosisLabel.setFont(font)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.kurtosisLabel)

        self.kurtosisValLabel = QLabel(self.centralwidget)
        self.kurtosisValLabel.setObjectName(u"kurtosisValLabel")
        self.kurtosisValLabel.setFont(font)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.kurtosisValLabel)

        self.antiKurtosisLabel = QLabel(self.centralwidget)
        self.antiKurtosisLabel.setObjectName(u"antiKurtosisLabel")
        self.antiKurtosisLabel.setFont(font)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.antiKurtosisLabel)

        self.antikurtosisValLabel = QLabel(self.centralwidget)
        self.antikurtosisValLabel.setObjectName(u"antikurtosisValLabel")
        self.antikurtosisValLabel.setFont(font)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.antikurtosisValLabel)

        self.minLabel = QLabel(self.centralwidget)
        self.minLabel.setObjectName(u"minLabel")
        self.minLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.minLabel)

        self.minValLabel = QLabel(self.centralwidget)
        self.minValLabel.setObjectName(u"minValLabel")
        self.minValLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.minValLabel)

        self.maxLabel = QLabel(self.centralwidget)
        self.maxLabel.setObjectName(u"maxLabel")
        self.maxLabel.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.maxLabel)

        self.maxValLabel = QLabel(self.centralwidget)
        self.maxValLabel.setObjectName(u"maxValLabel")
        self.maxValLabel.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.maxValLabel)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 12)
        self.verticalLayout.setStretch(2, 5)

        self.mainHorizontalLayout.addLayout(self.verticalLayout)

        self.canvasLayout = QGridLayout()
        self.canvasLayout.setObjectName(u"canvasLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.ecdfVerticalLayout = QVBoxLayout()
        self.ecdfVerticalLayout.setObjectName(u"ecdfVerticalLayout")

        self.verticalLayout_7.addLayout(self.ecdfVerticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.restoreCumulativePushButton = QPushButton(self.tab)
        self.restoreCumulativePushButton.setObjectName(u"restoreCumulativePushButton")
        font1 = QFont()
        font1.setPointSize(12)
        self.restoreCumulativePushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.restoreCumulativePushButton)

        self.restoredCumulativeInfoLayout = QFormLayout()
        self.restoredCumulativeInfoLayout.setObjectName(u"restoredCumulativeInfoLayout")

        self.horizontalLayout.addLayout(self.restoredCumulativeInfoLayout)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.verticalLayout_7.setStretch(0, 5)
        self.verticalLayout_7.setStretch(1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.verticalLayout_4 = QVBoxLayout(self.tab1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.densityPlotVerticalLayout = QVBoxLayout()
        self.densityPlotVerticalLayout.setObjectName(u"densityPlotVerticalLayout")

        self.verticalLayout_4.addLayout(self.densityPlotVerticalLayout)

        self.densityInfoHorizontalLayout = QHBoxLayout()
        self.densityInfoHorizontalLayout.setObjectName(u"densityInfoHorizontalLayout")
        self.densityClassInfoTableWidget = QTableWidget(self.tab1)
        self.densityClassInfoTableWidget.setObjectName(u"densityClassInfoTableWidget")

        self.densityInfoHorizontalLayout.addWidget(self.densityClassInfoTableWidget)

        self.densityInfoFolmLayout = QFormLayout()
        self.densityInfoFolmLayout.setObjectName(u"densityInfoFolmLayout")

        self.densityInfoHorizontalLayout.addLayout(self.densityInfoFolmLayout)

        self.densityInfoHorizontalLayout.setStretch(0, 1)
        self.densityInfoHorizontalLayout.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.densityInfoHorizontalLayout)

        self.verticalLayout_4.setStretch(0, 3)
        self.verticalLayout_4.setStretch(1, 1)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.verticalLayout_5 = QVBoxLayout(self.tab2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.paperPlotVerticalLayout = QVBoxLayout()
        self.paperPlotVerticalLayout.setObjectName(u"paperPlotVerticalLayout")

        self.verticalLayout_5.addLayout(self.paperPlotVerticalLayout)

        self.paperInfoHorizontalLayout = QHBoxLayout()
        self.paperInfoHorizontalLayout.setObjectName(u"paperInfoHorizontalLayout")

        self.verticalLayout_5.addLayout(self.paperInfoHorizontalLayout)

        self.verticalLayout_5.setStretch(0, 5)
        self.verticalLayout_5.setStretch(1, 1)
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.verticalLayout_6 = QVBoxLayout(self.tab3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.outliersPlotVerticalLayout = QVBoxLayout()
        self.outliersPlotVerticalLayout.setObjectName(u"outliersPlotVerticalLayout")

        self.verticalLayout_6.addLayout(self.outliersPlotVerticalLayout)

        self.outliersInfoHorizontalLayout = QHBoxLayout()
        self.outliersInfoHorizontalLayout.setObjectName(u"outliersInfoHorizontalLayout")
        self.outliersInfoHorizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.removeOutliersPushButton = QPushButton(self.tab3)
        self.removeOutliersPushButton.setObjectName(u"removeOutliersPushButton")
        self.removeOutliersPushButton.setFont(font1)

        self.outliersInfoHorizontalLayout.addWidget(self.removeOutliersPushButton)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.intervalLabel = QLabel(self.tab3)
        self.intervalLabel.setObjectName(u"intervalLabel")
        self.intervalLabel.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.intervalLabel)

        self.intervalValLabel = QLabel(self.tab3)
        self.intervalValLabel.setObjectName(u"intervalValLabel")
        self.intervalValLabel.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.intervalValLabel)


        self.outliersInfoHorizontalLayout.addLayout(self.formLayout_2)

        self.outliersInfoHorizontalLayout.setStretch(0, 3)
        self.outliersInfoHorizontalLayout.setStretch(1, 7)

        self.verticalLayout_6.addLayout(self.outliersInfoHorizontalLayout)

        self.verticalLayout_6.setStretch(0, 7)
        self.verticalLayout_6.setStretch(1, 1)
        self.tabWidget.addTab(self.tab3, "")

        self.canvasLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.mainHorizontalLayout.addLayout(self.canvasLayout)

        self.mainHorizontalLayout.setStretch(0, 3)
        self.mainHorizontalLayout.setStretch(1, 7)

        self.rootLayout.addLayout(self.mainHorizontalLayout)


        self.verticalLayout_2.addLayout(self.rootLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1600, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.filenamePushButton.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.countLabel.setText(QCoreApplication.translate("MainWindow", u"Count:", None))
        self.countValLabel.setText(QCoreApplication.translate("MainWindow", u"undefined", None))
        self.meanLabel.setText(QCoreApplication.translate("MainWindow", u"Mean:", None))
        self.meanValLabel.setText(QCoreApplication.translate("MainWindow", u"undefined", None))
        self.medianLabel.setText(QCoreApplication.translate("MainWindow", u"Median:", None))
        self.medianValLabel.setText(QCoreApplication.translate("MainWindow", u"undefined", None))
        self.stdLabel.setText(QCoreApplication.translate("MainWindow", u"std:", None))
        self.stdValLabel.setText(QCoreApplication.translate("MainWindow", u"undefined", None))
        self.skewnessLabel.setText(QCoreApplication.translate("MainWindow", u"Skewness:", None))
        self.skewnessValLabel.setText(QCoreApplication.translate("MainWindow", u"undefined", None))
        self.kurtosisLabel.setText(QCoreApplication.translate("MainWindow", u"Kurtosis:", None))
        self.kurtosisValLabel.setText(QCoreApplication.translate("MainWindow", u"undefined", None))
        self.antiKurtosisLabel.setText(QCoreApplication.translate("MainWindow", u"Anti kurtosis:", None))
        self.antikurtosisValLabel.setText(QCoreApplication.translate("MainWindow", u"undefined", None))
        self.minLabel.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.minValLabel.setText(QCoreApplication.translate("MainWindow", u"undefined", None))
        self.maxLabel.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.maxValLabel.setText(QCoreApplication.translate("MainWindow", u"undefined", None))
        self.restoreCumulativePushButton.setText(QCoreApplication.translate("MainWindow", u"Vosstanovit`", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cumulative distribution function", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Probability density function", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Probability paper", None))
        self.removeOutliersPushButton.setText(QCoreApplication.translate("MainWindow", u"Remove Outliers", None))
        self.intervalLabel.setText(QCoreApplication.translate("MainWindow", u"Interval: ", None))
        self.intervalValLabel.setText(QCoreApplication.translate("MainWindow", u"undefined", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"Outliers", None))
    # retranslateUi

