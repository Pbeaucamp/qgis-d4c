# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd4c_api_dialog_export.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject

class ExportWindow(QObject):
        exportEntered = QtCore.pyqtSignal(str)

class Ui_d4cAPIDialogExport(object):


    def __init__(self):
            
        self.export_window = ExportWindow()


    def setupUi(self, d4cAPIDialogExport):
        d4cAPIDialogExport.setObjectName("d4cAPIDialogExport")
        d4cAPIDialogExport.resize(341, 320)
        self.listResourceChoice = QtWidgets.QListWidget(d4cAPIDialogExport)
        self.listResourceChoice.setGeometry(QtCore.QRect(30, 40, 281, 221))
        self.listResourceChoice.setObjectName("listResourceChoice")
        self.label = QtWidgets.QLabel(d4cAPIDialogExport)
        self.label.setGeometry(QtCore.QRect(30, 20, 211, 16))
        self.label.setObjectName("label")
        self.validResourceChoice = QtWidgets.QPushButton(d4cAPIDialogExport)
        self.validResourceChoice.setGeometry(QtCore.QRect(250, 280, 75, 23))
        self.validResourceChoice.setObjectName("validResourceChoice")

        self.retranslateUi(d4cAPIDialogExport)
        QtCore.QMetaObject.connectSlotsByName(d4cAPIDialogExport)

        self.validResourceChoice.clicked.connect(self.validResourceChoiceClicked)   
    def retranslateUi(self, d4cAPIDialogExport):
        _translate = QtCore.QCoreApplication.translate
        d4cAPIDialogExport.setWindowTitle(_translate("d4cAPIDialogExport", "Choisir une ressource"))
        self.label.setText(_translate("d4cAPIDialogExport", "Selectionner une ressource"))
        self.validResourceChoice.setText(_translate("d4cAPIDialogExport", "Confirmer"))


    def validResourceChoiceClicked(self):
        item = self.listResourceChoice.currentItem()
        if item:
            self.export_window.exportEntered.emit(self.listResourceChoice.currentItem().text())
        else:
            self.export_window.exportEntered.emit('')