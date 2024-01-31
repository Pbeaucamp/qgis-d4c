# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd4c_api_dialog_editsites.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
import os

class EditSites(QObject):
    
    siteEntered = QtCore.pyqtSignal(str, str, str, str)


class Ui_EditSites(object):

    def __init__(self):
            
            self.edit_sites = EditSites()
        
    def setupUi(self, EditSites):
        self.plugin_dir = os.path.dirname(__file__)
        EditSites.setObjectName("EditSites")
        EditSites.resize(400, 369)

        self.validNewSite = QtWidgets.QPushButton(EditSites)
        self.validNewSite.setGeometry(QtCore.QRect(270, 300, 81, 31))
        self.validNewSite.setCheckable(True)
        self.validNewSite.setObjectName("validNewSite")

        self.label_5 = QtWidgets.QLabel(EditSites)
        self.label_5.setGeometry(QtCore.QRect(100, 170, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.siteUrl = QtWidgets.QLineEdit(EditSites)
        self.siteUrl.setGeometry(QtCore.QRect(50, 60, 271, 20))
        self.siteUrl.setObjectName("siteUrl")

        self.user_2 = QtWidgets.QLineEdit(EditSites)
        self.user_2.setGeometry(QtCore.QRect(70, 120, 231, 20))
        self.user_2.setText("")
        self.user_2.setObjectName("user_2")

        self.user = QtWidgets.QLineEdit(EditSites)
        self.user.setGeometry(QtCore.QRect(70, 190, 231, 20))
        self.user.setObjectName("user")

        self.label = QtWidgets.QLabel(EditSites)
        self.label.setGeometry(QtCore.QRect(50, 30, 21, 21))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(os.path.join(self.plugin_dir, 'img', 'internet_icon.png')))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        

        self.label_2 = QtWidgets.QLabel(EditSites)
        self.label_2.setGeometry(QtCore.QRect(70, 170, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setPixmap(QtGui.QPixmap(os.path.join(self.plugin_dir, 'img', 'usr_icon.png')))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(EditSites)
        self.label_3.setGeometry(QtCore.QRect(70, 240, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setPixmap(QtGui.QPixmap(os.path.join(self.plugin_dir, 'img', 'pwd_icon.png')))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(EditSites)
        self.label_4.setGeometry(QtCore.QRect(80, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")

        self.password = QtWidgets.QLineEdit(EditSites)
        self.password.setGeometry(QtCore.QRect(70, 260, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.password.setFont(font)
        self.password.setAutoFillBackground(False)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")

        self.label_6 = QtWidgets.QLabel(EditSites)
        self.label_6.setGeometry(QtCore.QRect(100, 240, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(EditSites)
        self.label_7.setGeometry(QtCore.QRect(70, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        

        self.retranslateUi(EditSites)
        QtCore.QMetaObject.connectSlotsByName(EditSites)

        self.validNewSite.clicked.connect(self.addSite)
    
    def retranslateUi(self, EditSites):
        _translate = QtCore.QCoreApplication.translate
        EditSites.setWindowTitle(_translate("EditSites", "Site"))
        self.validNewSite.setText(_translate("EditSites", "Valider"))
        self.label_5.setText(_translate("EditSites", "Utilisateur:"))
        self.siteUrl.setPlaceholderText(_translate("EditSites", "ex : https://website.data4citizen.com"))
        self.label_4.setText(_translate("EditSites", "URL du Site :"))
        self.label_6.setText(_translate("EditSites", "Mot de Passe :"))
        self.label_7.setText(_translate("EditSites", "Nom :"))


    def addSite(self):
        if self.siteUrl.text().endswith('/') or self.siteUrl.text().endswith(' '):
            self.siteUrl.setText(self.siteUrl.text()[:-1])
        if self.siteUrl.text().startswith(' '):
            self.siteUrl.setText(self.siteUrl.text()[1:])
        if self.user.text().startswith(' '):
            self.user.setText(self.user.text()[1:])
        if self.user.text().endswith(' '):
            self.user.setText(self.user.text()[:-1])
        
        if self.password.text().startswith(' '):
            self.password.setText(self.password.text()[1:])
        if self.password.text().endswith(' '):
            self.password.setText(self.password.text()[:-1])
        self.edit_sites.siteEntered.emit(self.siteUrl.text(), self.user_2.text(), self.user.text(), self.password.text())