# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd4c_api_dialog_changemetadatas.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_changeMetadatas(object):

    def __init__(self):
        
        
        self.themes_checkboxes = []
        self.tags_checkboxes = []
        self.scrollLayout2 = QtWidgets.QVBoxLayout()
        self.scrollLayout3 = QtWidgets.QVBoxLayout()
        self.lic = None
        self.desc = None

    def setupUi(self, changeMetadatas):
        changeMetadatas.setObjectName("changeMetadatas")
        changeMetadatas.resize(634, 474)
        self.newDatasetName = QtWidgets.QLineEdit(changeMetadatas)
        self.newDatasetName.setGeometry(QtCore.QRect(50, 50, 291, 20))
        self.newDatasetName.setObjectName("newDatasetName")
        self.label_3 = QtWidgets.QLabel(changeMetadatas)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 141, 16))
        self.label_3.setObjectName("label_3")
        self.orgCombobox = QtWidgets.QComboBox(changeMetadatas)
        self.orgCombobox.setGeometry(QtCore.QRect(50, 100, 291, 22))
        self.orgCombobox.setObjectName("orgCombobox")
        self.scrollArea = QtWidgets.QScrollArea(changeMetadatas)
        self.scrollArea.setGeometry(QtCore.QRect(350, 180, 201, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 199, 219))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.label_5 = QtWidgets.QLabel(changeMetadatas)
        self.label_5.setGeometry(QtCore.QRect(80, 160, 47, 13))
        self.label_5.setObjectName("label_5")
        self.hideInCatalogue = QtWidgets.QCheckBox(changeMetadatas)
        self.hideInCatalogue.setGeometry(QtCore.QRect(380, 50, 151, 17))
        self.hideInCatalogue.setObjectName("hideInCatalogue")
        self.label_6 = QtWidgets.QLabel(changeMetadatas)
        self.label_6.setGeometry(QtCore.QRect(350, 160, 51, 16))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(changeMetadatas)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 291, 16))
        self.label_2.setObjectName("label_2")
        self.themeScrollArea = QtWidgets.QScrollArea(changeMetadatas)
        self.themeScrollArea.setGeometry(QtCore.QRect(80, 180, 191, 221))
        self.themeScrollArea.setWidgetResizable(True)
        self.themeScrollArea.setObjectName("themeScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 189, 219))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.themeScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.hideInMap = QtWidgets.QCheckBox(changeMetadatas)
        self.hideInMap.setGeometry(QtCore.QRect(380, 110, 211, 17))
        self.hideInMap.setObjectName("hideInMap")
        self.hideInGraph = QtWidgets.QCheckBox(changeMetadatas)
        self.hideInGraph.setGeometry(QtCore.QRect(380, 80, 211, 17))
        self.hideInGraph.setObjectName("hideInGraph")
        self.checkPrivate = QtWidgets.QCheckBox(changeMetadatas)
        self.checkPrivate.setGeometry(QtCore.QRect(50, 130, 70, 17))
        self.checkPrivate.setObjectName("checkPrivate")
        self.checkChecked = QtWidgets.QCheckBox(changeMetadatas)
        self.checkChecked.setGeometry(QtCore.QRect(350, 400, 101, 17))
        self.checkChecked.setObjectName("checkChecked")
        self.keywordSearch = QtWidgets.QLineEdit(changeMetadatas)
        self.keywordSearch.setGeometry(QtCore.QRect(410, 160, 141, 20))
        self.keywordSearch.setObjectName("keywordSearch")
        self.keywordSearch.setPlaceholderText("Rechercher un mot-clef")
        self.pushOk = QtWidgets.QPushButton(changeMetadatas)
        self.pushOk.setGeometry(QtCore.QRect(460, 430, 75, 31))
        self.pushOk.setObjectName("pushOk")
        self.pushCancel = QtWidgets.QPushButton(changeMetadatas)
        self.pushCancel.setGeometry(QtCore.QRect(540, 430, 75, 31))
        self.pushCancel.setObjectName("pushCancel")


        self.retranslateUi(changeMetadatas)
        QtCore.QMetaObject.connectSlotsByName(changeMetadatas)

    def retranslateUi(self, changeMetadatas):
        _translate = QtCore.QCoreApplication.translate
        changeMetadatas.setWindowTitle(_translate("changeMetadatas", "Changer les métadonnées"))
        self.label_3.setText(_translate("changeMetadatas", "Nom du Jeu de donnée :"))
        self.label_5.setText(_translate("changeMetadatas", "Thèmes :"))
        self.hideInCatalogue.setText(_translate("changeMetadatas", "Cacher dans le catalogue"))
        self.label_6.setText(_translate("changeMetadatas", "Mot-clefs :"))
        self.label_2.setText(_translate("changeMetadatas", "Organisation :"))
        self.hideInMap.setText(_translate("changeMetadatas", "Cacher dans l\'interface des cartes"))
        self.hideInGraph.setText(_translate("changeMetadatas", "Cacher dans l\'interface des graphiques"))
        self.checkPrivate.setText(_translate("changeMetadatas", "Privée"))
        self.checkChecked.setText(_translate("changeMetadatas", "Afficher cochés"))
        self.pushOk.setText(_translate("changeMetadatas", "Ok"))
        self.pushCancel.setText(_translate("changeMetadatas", "Annuler"))
        self.keywordSearch.setPlaceholderText(_translate("changeMetadatas", "Rechercher un mot-clef"))
