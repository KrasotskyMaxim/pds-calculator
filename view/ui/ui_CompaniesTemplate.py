# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/maks/myfolder/BSUIR/PBZ/lab2/solution/pds-calculator/view/ui/CompaniesTemplate.ui'
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
        self.SelectCompanyComboBox = QtWidgets.QComboBox(CompaniesForm)
        self.SelectCompanyComboBox.setGeometry(QtCore.QRect(10, 40, 171, 25))
        self.SelectCompanyComboBox.setObjectName("SelectCompanyComboBox")
        self.CompaniesLabel = QtWidgets.QLabel(CompaniesForm)
        self.CompaniesLabel.setGeometry(QtCore.QRect(60, 10, 81, 20))
        self.CompaniesLabel.setObjectName("CompaniesLabel")
        self.CompanyInfoTextBrowser = QtWidgets.QTextBrowser(CompaniesForm)
        self.CompanyInfoTextBrowser.setGeometry(QtCore.QRect(10, 80, 271, 301))
        self.CompanyInfoTextBrowser.setObjectName("CompanyInfoTextBrowser")
        self.AddCompanyPushButton = QtWidgets.QPushButton(CompaniesForm)
        self.AddCompanyPushButton.setGeometry(QtCore.QRect(190, 40, 89, 25))
        self.AddCompanyPushButton.setObjectName("AddCompanyPushButton")
        self.EditCompanyPushButton = QtWidgets.QPushButton(CompaniesForm)
        self.EditCompanyPushButton.setGeometry(QtCore.QRect(10, 390, 89, 25))
        self.EditCompanyPushButton.setObjectName("EditCompanyPushButton")
        self.DeleteCompanyPushButton = QtWidgets.QPushButton(CompaniesForm)
        self.DeleteCompanyPushButton.setGeometry(QtCore.QRect(110, 390, 89, 25))
        self.DeleteCompanyPushButton.setObjectName("DeleteCompanyPushButton")
        self.CompanyBackPushButton = QtWidgets.QPushButton(CompaniesForm)
        self.CompanyBackPushButton.setGeometry(QtCore.QRect(20, 760, 89, 25))
        self.CompanyBackPushButton.setObjectName("CompanyBackPushButton")
        self.ShowCompanyPushButton = QtWidgets.QPushButton(CompaniesForm)
        self.ShowCompanyPushButton.setGeometry(QtCore.QRect(290, 40, 89, 25))
        self.ShowCompanyPushButton.setObjectName("ShowCompanyPushButton")

        self.retranslateUi(CompaniesForm)
        QtCore.QMetaObject.connectSlotsByName(CompaniesForm)

    def retranslateUi(self, CompaniesForm):
        _translate = QtCore.QCoreApplication.translate
        CompaniesForm.setWindowTitle(_translate("CompaniesForm", "Form"))
        self.CompaniesLabel.setText(_translate("CompaniesForm", "Companies"))
        self.AddCompanyPushButton.setText(_translate("CompaniesForm", "Add"))
        self.EditCompanyPushButton.setText(_translate("CompaniesForm", "Edit"))
        self.DeleteCompanyPushButton.setText(_translate("CompaniesForm", "Delete"))
        self.CompanyBackPushButton.setText(_translate("CompaniesForm", "Back"))
        self.ShowCompanyPushButton.setText(_translate("CompaniesForm", "Show"))