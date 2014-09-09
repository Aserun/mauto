# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Sep  8 21:10:53 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(364, 406)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.listing = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listing.sizePolicy().hasHeightForWidth())
        self.listing.setSizePolicy(sizePolicy)
        self.listing.setMinimumSize(QtCore.QSize(120, 0))
        self.listing.setObjectName("listing")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.listing)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.filter = QtGui.QLineEdit(self.listing)
        self.filter.setObjectName("filter")
        self.verticalLayout_2.addWidget(self.filter)
        self.macros = QtGui.QTableWidget(self.listing)
        self.macros.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.macros.setShowGrid(False)
        self.macros.setRowCount(0)
        self.macros.setObjectName("macros")
        self.macros.setColumnCount(1)
        self.macros.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.macros.setHorizontalHeaderItem(0, item)
        self.macros.horizontalHeader().setVisible(False)
        self.macros.horizontalHeader().setStretchLastSection(True)
        self.macros.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.macros)
        self.properties = QtGui.QFrame(self.splitter)
        self.properties.setEnabled(True)
        self.properties.setObjectName("properties")
        self.verticalLayout = QtGui.QVBoxLayout(self.properties)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputs = QtGui.QTableWidget(self.properties)
        self.inputs.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputs.sizePolicy().hasHeightForWidth())
        self.inputs.setSizePolicy(sizePolicy)
        self.inputs.setMinimumSize(QtCore.QSize(220, 0))
        self.inputs.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.inputs.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.inputs.setShowGrid(True)
        self.inputs.setObjectName("inputs")
        self.inputs.setColumnCount(2)
        self.inputs.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.inputs.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.inputs.setHorizontalHeaderItem(1, item)
        self.inputs.horizontalHeader().setVisible(True)
        self.inputs.horizontalHeader().setDefaultSectionSize(80)
        self.inputs.horizontalHeader().setStretchLastSection(True)
        self.inputs.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.inputs)
        self.from_selection = QtGui.QCheckBox(self.properties)
        self.from_selection.setChecked(True)
        self.from_selection.setObjectName("from_selection")
        self.verticalLayout.addWidget(self.from_selection)
        self.action = QtGui.QPushButton(self.properties)
        self.action.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action.sizePolicy().hasHeightForWidth())
        self.action.setSizePolicy(sizePolicy)
        self.action.setMinimumSize(QtCore.QSize(0, 120))
        self.action.setText("")
        self.action.setIconSize(QtCore.QSize(64, 64))
        self.action.setFlat(True)
        self.action.setObjectName("action")
        self.verticalLayout.addWidget(self.action)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.macros, self.filter)
        MainWindow.setTabOrder(self.filter, self.inputs)
        MainWindow.setTabOrder(self.inputs, self.from_selection)
        MainWindow.setTabOrder(self.from_selection, self.action)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "mauto", None, QtGui.QApplication.UnicodeUTF8))
        self.filter.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Filter o create new", None, QtGui.QApplication.UnicodeUTF8))
        self.macros.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Names", None, QtGui.QApplication.UnicodeUTF8))
        self.inputs.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.inputs.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.from_selection.setText(QtGui.QApplication.translate("MainWindow", "Inputs from selection", None, QtGui.QApplication.UnicodeUTF8))

