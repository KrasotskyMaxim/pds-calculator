# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/maks/myfolder/BSUIR/PBZ/lab2/solution/pds-calculator/view/ui/CanalizationsTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CompaniesForm(object):
    def __init__(self, form) -> None:
        self.setupUi(CompaniesForm=form)
    
    def setupUi(self, CompaniesForm):
        CompaniesForm.setObjectName("CompaniesForm")
        CompaniesForm.resize(600, 800)
        self.SelectCanalizationComboBox = QtWidgets.QComboBox(CompaniesForm)
        self.SelectCanalizationComboBox.setGeometry(QtCore.QRect(10, 40, 171, 25))
        self.SelectCanalizationComboBox.setObjectName("SelectCanalizationComboBox")
        self.CanalizationsLabel = QtWidgets.QLabel(CompaniesForm)
        self.CanalizationsLabel.setGeometry(QtCore.QRect(60, 10, 91, 20))
        self.CanalizationsLabel.setObjectName("CanalizationsLabel")
        self.CanalizationInfoTextBrowser = QtWidgets.QTextBrowser(CompaniesForm)
        self.CanalizationInfoTextBrowser.setGeometry(QtCore.QRect(10, 80, 271, 301))
        self.CanalizationInfoTextBrowser.setObjectName("CanalizationInfoTextBrowser")
        self.AddCanalizationPushButton = QtWidgets.QPushButton(CompaniesForm)
        self.AddCanalizationPushButton.setGeometry(QtCore.QRect(190, 40, 89, 25))
        self.AddCanalizationPushButton.setObjectName("AddCanalizationPushButton")
        self.EditCanalizationPushButton = QtWidgets.QPushButton(CompaniesForm)
        self.EditCanalizationPushButton.setGeometry(QtCore.QRect(10, 390, 89, 25))
        self.EditCanalizationPushButton.setObjectName("EditCanalizationPushButton")
        self.DeleteCanalizationPushButton = QtWidgets.QPushButton(CompaniesForm)
        self.DeleteCanalizationPushButton.setGeometry(QtCore.QRect(110, 390, 89, 25))
        self.DeleteCanalizationPushButton.setObjectName("DeleteCanalizationPushButton")
        self.CanalizationBackPushButton = QtWidgets.QPushButton(CompaniesForm)
        self.CanalizationBackPushButton.setGeometry(QtCore.QRect(10, 760, 89, 25))
        self.CanalizationBackPushButton.setObjectName("CanalizationBackPushButton")
        self.ShowCanalizationPushButton = QtWidgets.QPushButton(CompaniesForm)
        self.ShowCanalizationPushButton.setGeometry(QtCore.QRect(290, 40, 89, 25))
        self.ShowCanalizationPushButton.setObjectName("ShowCanalizationPushButton")

        self.retranslateUi(CompaniesForm)
        QtCore.QMetaObject.connectSlotsByName(CompaniesForm)

    def retranslateUi(self, CompaniesForm):
        _translate = QtCore.QCoreApplication.translate
        CompaniesForm.setWindowTitle(_translate("CompaniesForm", "Form"))
        self.CanalizationsLabel.setText(_translate("CompaniesForm", "Canalizations"))
        self.AddCanalizationPushButton.setText(_translate("CompaniesForm", "Add"))
        self.EditCanalizationPushButton.setText(_translate("CompaniesForm", "Edit"))
        self.DeleteCanalizationPushButton.setText(_translate("CompaniesForm", "Delete"))
        self.CanalizationBackPushButton.setText(_translate("CompaniesForm", "Back"))
        self.ShowCanalizationPushButton.setText(_translate("CompaniesForm", "Show"))