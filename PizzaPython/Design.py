# Copyright (c) 2022 RodKingroo

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(262, 290)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PizzaEnumCombo = QtWidgets.QComboBox(self.centralwidget)
        self.PizzaEnumCombo.setGeometry(QtCore.QRect(100, 15, 150, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.PizzaEnumCombo.setFont(font)
        self.PizzaEnumCombo.setObjectName("PizzaEnumCombo")
        self.LabelUOrder = QtWidgets.QLabel(self.centralwidget)
        self.LabelUOrder.setGeometry(QtCore.QRect(15, 15, 75, 16))
        self.LabelUOrder.setObjectName("LabelUOrder")
        self.YourPizza = QtWidgets.QLineEdit(self.centralwidget)
        self.YourPizza.setEnabled(True)
        self.YourPizza.setGeometry(QtCore.QRect(100, 260, 150, 20))
        self.YourPizza.setText("")
        self.YourPizza.setObjectName("YourPizza")
        self.LabelUPizza = QtWidgets.QLabel(self.centralwidget)
        self.LabelUPizza.setGeometry(QtCore.QRect(15, 260, 75, 16))
        self.LabelUPizza.setObjectName("LabelUPizza")
        self.InfoCooking = QtWidgets.QTextEdit(self.centralwidget)
        self.InfoCooking.setGeometry(QtCore.QRect(15, 80, 235, 165))
        self.InfoCooking.setObjectName("InfoCooking")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(15, 45, 235, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LabelUOrder.setText(_translate("MainWindow", "Your order:"))
        self.LabelUPizza.setText(_translate("MainWindow", "Your pizza:"))