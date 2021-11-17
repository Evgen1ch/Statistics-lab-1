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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.restoreCumulativePushButton = QPushButton(self.tab)
        self.restoreCumulativePushButton.setObjectName(u"restoreCumulativePushButton")
        self.restoreCumulativePushButton.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(12)
        self.restoreCumulativePushButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.restoreCumulativePushButton)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.restoredCumulativeInfoLayout = QFormLayout()
        self.restoredCumulativeInfoLayout.setObjectName(u"restoredCumulativeInfoLayout")
        self.restoredCumulativeInfoLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.chiSquareLabel = QLabel(self.tab)
        self.chiSquareLabel.setObjectName(u"chiSquareLabel")

        self.restoredCumulativeInfoLayout.setWidget(0, QFormLayout.LabelRole, self.chiSquareLabel)

        self.chiSquareLineEdit = QLineEdit(self.tab)
        self.chiSquareLineEdit.setObjectName(u"chiSquareLineEdit")
        self.chiSquareLineEdit.setReadOnly(True)

        self.restoredCumulativeInfoLayout.setWidget(0, QFormLayout.FieldRole, self.chiSquareLineEdit)

        self.critChiSquareLabel = QLabel(self.tab)
        self.critChiSquareLabel.setObjectName(u"critChiSquareLabel")

        self.restoredCumulativeInfoLayout.setWidget(1, QFormLayout.LabelRole, self.critChiSquareLabel)

        self.critChiSquareLineEdit = QLineEdit(self.tab)
        self.critChiSquareLineEdit.setObjectName(u"critChiSquareLineEdit")
        self.critChiSquareLineEdit.setReadOnly(True)

        self.restoredCumulativeInfoLayout.setWidget(1, QFormLayout.FieldRole, self.critChiSquareLineEdit)

        self.confidenceIntervallForALabel = QLabel(self.tab)
        self.confidenceIntervallForALabel.setObjectName(u"confidenceIntervallForALabel")

        self.restoredCumulativeInfoLayout.setWidget(5, QFormLayout.LabelRole, self.confidenceIntervallForALabel)

        self.confidenceIntervallForALineEdit = QLineEdit(self.tab)
        self.confidenceIntervallForALineEdit.setObjectName(u"confidenceIntervallForALineEdit")
        self.confidenceIntervallForALineEdit.setReadOnly(True)

        self.restoredCumulativeInfoLayout.setWidget(5, QFormLayout.FieldRole, self.confidenceIntervallForALineEdit)

        self.confidenceIntervalForBLabel = QLabel(self.tab)
        self.confidenceIntervalForBLabel.setObjectName(u"confidenceIntervalForBLabel")

        self.restoredCumulativeInfoLayout.setWidget(8, QFormLayout.LabelRole, self.confidenceIntervalForBLabel)

        self.confidenceIntervalForBLineEdit = QLineEdit(self.tab)
        self.confidenceIntervalForBLineEdit.setObjectName(u"confidenceIntervalForBLineEdit")
        self.confidenceIntervalForBLineEdit.setReadOnly(True)

        self.restoredCumulativeInfoLayout.setWidget(8, QFormLayout.FieldRole, self.confidenceIntervalForBLineEdit)

        self.isDistrubutionProbableLabel = QLabel(self.tab)
        self.isDistrubutionProbableLabel.setObjectName(u"isDistrubutionProbableLabel")

        self.restoredCumulativeInfoLayout.setWidget(3, QFormLayout.LabelRole, self.isDistrubutionProbableLabel)

        self.isDistrubutionProbableLineEdit = QLineEdit(self.tab)
        self.isDistrubutionProbableLineEdit.setObjectName(u"isDistrubutionProbableLineEdit")
        self.isDistrubutionProbableLineEdit.setReadOnly(True)

        self.restoredCumulativeInfoLayout.setWidget(3, QFormLayout.FieldRole, self.isDistrubutionProbableLineEdit)

        self.aLabel_2 = QLabel(self.tab)
        self.aLabel_2.setObjectName(u"aLabel_2")

        self.restoredCumulativeInfoLayout.setWidget(4, QFormLayout.LabelRole, self.aLabel_2)

        self.aLineEdit_2 = QLineEdit(self.tab)
        self.aLineEdit_2.setObjectName(u"aLineEdit_2")
        self.aLineEdit_2.setReadOnly(True)

        self.restoredCumulativeInfoLayout.setWidget(4, QFormLayout.FieldRole, self.aLineEdit_2)

        self.bLabel_2 = QLabel(self.tab)
        self.bLabel_2.setObjectName(u"bLabel_2")

        self.restoredCumulativeInfoLayout.setWidget(7, QFormLayout.LabelRole, self.bLabel_2)

        self.bLineEdit_2 = QLineEdit(self.tab)
        self.bLineEdit_2.setObjectName(u"bLineEdit_2")
        self.bLineEdit_2.setReadOnly(True)

        self.restoredCumulativeInfoLayout.setWidget(7, QFormLayout.FieldRole, self.bLineEdit_2)

        self.aStdLabel = QLabel(self.tab)
        self.aStdLabel.setObjectName(u"aStdLabel")

        self.restoredCumulativeInfoLayout.setWidget(6, QFormLayout.LabelRole, self.aStdLabel)

        self.aStdLineEdit = QLineEdit(self.tab)
        self.aStdLineEdit.setObjectName(u"aStdLineEdit")

        self.restoredCumulativeInfoLayout.setWidget(6, QFormLayout.FieldRole, self.aStdLineEdit)

        self.bStdLabel = QLabel(self.tab)
        self.bStdLabel.setObjectName(u"bStdLabel")

        self.restoredCumulativeInfoLayout.setWidget(9, QFormLayout.LabelRole, self.bStdLabel)

        self.bStdLineEdit = QLineEdit(self.tab)
        self.bStdLineEdit.setObjectName(u"bStdLineEdit")

        self.restoredCumulativeInfoLayout.setWidget(9, QFormLayout.FieldRole, self.bStdLineEdit)

        self.pValueLabel = QLabel(self.tab)
        self.pValueLabel.setObjectName(u"pValueLabel")

        self.restoredCumulativeInfoLayout.setWidget(2, QFormLayout.LabelRole, self.pValueLabel)

        self.pValueLineEdit = QLineEdit(self.tab)
        self.pValueLineEdit.setObjectName(u"pValueLineEdit")

        self.restoredCumulativeInfoLayout.setWidget(2, QFormLayout.FieldRole, self.pValueLineEdit)


        self.horizontalLayout.addLayout(self.restoredCumulativeInfoLayout)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.verticalLayout_7.setStretch(0, 7)
        self.verticalLayout_7.setStretch(1, 2)
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
        self.histClassesLabel = QLabel(self.tab1)
        self.histClassesLabel.setObjectName(u"histClassesLabel")
        self.histClassesLabel.setFont(font)

        self.densityInfoFolmLayout.setWidget(0, QFormLayout.LabelRole, self.histClassesLabel)

        self.histClassesSpinBox = QSpinBox(self.tab1)
        self.histClassesSpinBox.setObjectName(u"histClassesSpinBox")
        self.histClassesSpinBox.setFont(font)
        self.histClassesSpinBox.setMinimum(1)
        self.histClassesSpinBox.setMaximum(100)

        self.densityInfoFolmLayout.setWidget(0, QFormLayout.FieldRole, self.histClassesSpinBox)

        self.bandwidthLabel = QLabel(self.tab1)
        self.bandwidthLabel.setObjectName(u"bandwidthLabel")
        self.bandwidthLabel.setFont(font)

        self.densityInfoFolmLayout.setWidget(1, QFormLayout.LabelRole, self.bandwidthLabel)

        self.kdeBandwidthSpinBox = QDoubleSpinBox(self.tab1)
        self.kdeBandwidthSpinBox.setObjectName(u"kdeBandwidthSpinBox")
        self.kdeBandwidthSpinBox.setFont(font)
        self.kdeBandwidthSpinBox.setDecimals(7)
        self.kdeBandwidthSpinBox.setMinimum(0.001000000000000)
        self.kdeBandwidthSpinBox.setSingleStep(0.001000000000000)
        self.kdeBandwidthSpinBox.setValue(3.000000000000000)

        self.densityInfoFolmLayout.setWidget(1, QFormLayout.FieldRole, self.kdeBandwidthSpinBox)

        self.updateHistKdePushButton = QPushButton(self.tab1)
        self.updateHistKdePushButton.setObjectName(u"updateHistKdePushButton")
        font1 = QFont()
        font1.setPointSize(10)
        self.updateHistKdePushButton.setFont(font1)

        self.densityInfoFolmLayout.setWidget(2, QFormLayout.FieldRole, self.updateHistKdePushButton)


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
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setContentsMargins(10, -1, 10, -1)
        self.aLabel = QLabel(self.tab2)
        self.aLabel.setObjectName(u"aLabel")
        self.aLabel.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.aLabel)

        self.aLineEdit = QLineEdit(self.tab2)
        self.aLineEdit.setObjectName(u"aLineEdit")
        self.aLineEdit.setFont(font)
        self.aLineEdit.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.aLineEdit)

        self.bLabel = QLabel(self.tab2)
        self.bLabel.setObjectName(u"bLabel")
        self.bLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.bLabel)

        self.bLineEdit = QLineEdit(self.tab2)
        self.bLineEdit.setObjectName(u"bLineEdit")
        self.bLineEdit.setFont(font)
        self.bLineEdit.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.bLineEdit)


        self.paperInfoHorizontalLayout.addLayout(self.formLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fillWidget = QWidget(self.tab2)
        self.fillWidget.setObjectName(u"fillWidget")
        self.probPaperInfo = QLabel(self.fillWidget)
        self.probPaperInfo.setObjectName(u"probPaperInfo")
        self.probPaperInfo.setGeometry(QRect(10, 10, 621, 31))
        self.probPaperInfo.setFont(font)

        self.horizontalLayout_3.addWidget(self.fillWidget)


        self.paperInfoHorizontalLayout.addLayout(self.horizontalLayout_3)

        self.paperInfoHorizontalLayout.setStretch(0, 2)
        self.paperInfoHorizontalLayout.setStretch(1, 3)

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
        self.formLayout_2.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.intervalLabel = QLabel(self.tab3)
        self.intervalLabel.setObjectName(u"intervalLabel")
        self.intervalLabel.setFont(font)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.intervalLabel)

        self.intervalValLabel = QLabel(self.tab3)
        self.intervalValLabel.setObjectName(u"intervalValLabel")
        self.intervalValLabel.setFont(font)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.intervalValLabel)

        self.kSpinBox = QDoubleSpinBox(self.tab3)
        self.kSpinBox.setObjectName(u"kSpinBox")
        self.kSpinBox.setFont(font)
        self.kSpinBox.setDecimals(7)
        self.kSpinBox.setMinimum(0.001000000000000)
        self.kSpinBox.setSingleStep(0.001000000000000)
        self.kSpinBox.setValue(1.500000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.kSpinBox)

        self.kLabel = QLabel(self.tab3)
        self.kLabel.setObjectName(u"kLabel")
        self.kLabel.setFont(font)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.kLabel)

        self.updateKPushButton = QPushButton(self.tab3)
        self.updateKPushButton.setObjectName(u"updateKPushButton")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.updateKPushButton)


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
        self.filenameLineEdit.setText(QCoreApplication.translate("MainWindow", u"data_lab1\\70\\norm.txt", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.filenamePushButton.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.restoreCumulativePushButton.setText(QCoreApplication.translate("MainWindow", u"Restore Weibull distribution", None))
        self.chiSquareLabel.setText(QCoreApplication.translate("MainWindow", u"Chi square: ", None))
        self.critChiSquareLabel.setText(QCoreApplication.translate("MainWindow", u"Crit. chi square:", None))
        self.confidenceIntervallForALabel.setText(QCoreApplication.translate("MainWindow", u"Confidence intervall for a:", None))
        self.confidenceIntervalForBLabel.setText(QCoreApplication.translate("MainWindow", u"Confidence interval for b:", None))
        self.isDistrubutionProbableLabel.setText(QCoreApplication.translate("MainWindow", u"Is Weibull:", None))
        self.aLabel_2.setText(QCoreApplication.translate("MainWindow", u"a: ", None))
        self.bLabel_2.setText(QCoreApplication.translate("MainWindow", u"b: ", None))
        self.aStdLabel.setText(QCoreApplication.translate("MainWindow", u"a std:", None))
        self.bStdLabel.setText(QCoreApplication.translate("MainWindow", u"b std:", None))
        self.pValueLabel.setText(QCoreApplication.translate("MainWindow", u"P-value:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cumulative distribution function", None))
        self.histClassesLabel.setText(QCoreApplication.translate("MainWindow", u"Histogram classes:", None))
        self.bandwidthLabel.setText(QCoreApplication.translate("MainWindow", u"KDE bandwidth:", None))
        self.updateHistKdePushButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Probability density function", None))
        self.aLabel.setText(QCoreApplication.translate("MainWindow", u"a:", None))
        self.bLabel.setText(QCoreApplication.translate("MainWindow", u"b:", None))
        self.probPaperInfo.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Probability paper", None))
        self.removeOutliersPushButton.setText(QCoreApplication.translate("MainWindow", u"Remove Outliers", None))
        self.intervalLabel.setText(QCoreApplication.translate("MainWindow", u"Interval: ", None))
        self.intervalValLabel.setText(QCoreApplication.translate("MainWindow", u"undefined", None))
        self.kLabel.setText(QCoreApplication.translate("MainWindow", u"K = ", None))
        self.updateKPushButton.setText(QCoreApplication.translate("MainWindow", u"Change k", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"Outliers", None))
    # retranslateUi

