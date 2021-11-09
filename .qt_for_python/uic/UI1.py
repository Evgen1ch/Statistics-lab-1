# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI1.ui'
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

        self.ditributionStatisticsVerticalLayout = QVBoxLayout()
        self.ditributionStatisticsVerticalLayout.setObjectName(u"ditributionStatisticsVerticalLayout")
        self.distributionStatisticsTableWidget = QTableWidget(self.centralwidget)
        self.distributionStatisticsTableWidget.setObjectName(u"distributionStatisticsTableWidget")

        self.ditributionStatisticsVerticalLayout.addWidget(self.distributionStatisticsTableWidget)


        self.verticalLayout.addLayout(self.ditributionStatisticsVerticalLayout)

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
        font = QFont()
        font.setPointSize(12)
        self.restoreCumulativePushButton.setFont(font)

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
        self.removeOutliersPushButton.setFont(font)

        self.outliersInfoHorizontalLayout.addWidget(self.removeOutliersPushButton)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.intervalLabel = QLabel(self.tab3)
        self.intervalLabel.setObjectName(u"intervalLabel")
        self.intervalLabel.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.intervalLabel)

        self.intervalValLabel = QLabel(self.tab3)
        self.intervalValLabel.setObjectName(u"intervalValLabel")
        self.intervalValLabel.setFont(font)

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
        self.restoreCumulativePushButton.setText(QCoreApplication.translate("MainWindow", u"Vosstanovit`", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cumulative distribution function", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Probability density function", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Probability paper", None))
        self.removeOutliersPushButton.setText(QCoreApplication.translate("MainWindow", u"Remove Outliers", None))
        self.intervalLabel.setText(QCoreApplication.translate("MainWindow", u"Interval: ", None))
        self.intervalValLabel.setText(QCoreApplication.translate("MainWindow", u"undefined", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"Outliers", None))
    # retranslateUi

