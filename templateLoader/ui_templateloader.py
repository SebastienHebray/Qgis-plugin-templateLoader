# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templateloader.ui'
#
# Created: Mon Sep  8 18:08:26 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TemplateLoader(object):
    def setupUi(self, TemplateLoader):
        TemplateLoader.setObjectName(_fromUtf8("TemplateLoader"))
        TemplateLoader.resize(464, 446)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/templateloader/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TemplateLoader.setWindowIcon(icon)
        TemplateLoader.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.buttonBox = QtGui.QDialogButtonBox(TemplateLoader)
        self.buttonBox.setGeometry(QtCore.QRect(100, 400, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.mainTitle_label = QtGui.QLabel(TemplateLoader)
        self.mainTitle_label.setGeometry(QtCore.QRect(20, 100, 66, 17))
        self.mainTitle_label.setObjectName(_fromUtf8("mainTitle_label"))
        self.subTitle_label = QtGui.QLabel(TemplateLoader)
        self.subTitle_label.setGeometry(QtCore.QRect(20, 140, 71, 17))
        self.subTitle_label.setObjectName(_fromUtf8("subTitle_label"))
        self.txtSource_label = QtGui.QLabel(TemplateLoader)
        self.txtSource_label.setGeometry(QtCore.QRect(20, 300, 71, 17))
        self.txtSource_label.setObjectName(_fromUtf8("txtSource_label"))
        self.txtSource = QtGui.QPlainTextEdit(TemplateLoader)
        self.txtSource.setGeometry(QtCore.QRect(100, 300, 341, 91))
        self.txtSource.setObjectName(_fromUtf8("txtSource"))
        self.layoutWidget = QtGui.QWidget(TemplateLoader)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 170, 141, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.iNumCarte_label = QtGui.QLabel(self.layoutWidget)
        self.iNumCarte_label.setObjectName(_fromUtf8("iNumCarte_label"))
        self.horizontalLayout.addWidget(self.iNumCarte_label)
        self.iNumCarte = QtGui.QSpinBox(self.layoutWidget)
        self.iNumCarte.setObjectName(_fromUtf8("iNumCarte"))
        self.horizontalLayout.addWidget(self.iNumCarte)
        self.txtsubTitle = QtGui.QPlainTextEdit(TemplateLoader)
        self.txtsubTitle.setGeometry(QtCore.QRect(100, 130, 341, 31))
        self.txtsubTitle.setObjectName(_fromUtf8("txtsubTitle"))
        self.layoutWidget1 = QtGui.QWidget(TemplateLoader)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 421, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cmbTemplate_label = QtGui.QLabel(self.layoutWidget1)
        self.cmbTemplate_label.setObjectName(_fromUtf8("cmbTemplate_label"))
        self.horizontalLayout_3.addWidget(self.cmbTemplate_label)
        self.cmbTemplate = QtGui.QComboBox(self.layoutWidget1)
        self.cmbTemplate.setObjectName(_fromUtf8("cmbTemplate"))
        self.horizontalLayout_3.addWidget(self.cmbTemplate)
        self.layoutWidget2 = QtGui.QWidget(TemplateLoader)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 50, 421, 29))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.cmbScale_label = QtGui.QLabel(self.layoutWidget2)
        self.cmbScale_label.setObjectName(_fromUtf8("cmbScale_label"))
        self.horizontalLayout_4.addWidget(self.cmbScale_label)
        self.cmbScale = QtGui.QComboBox(self.layoutWidget2)
        self.cmbScale.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.cmbScale.setObjectName(_fromUtf8("cmbScale"))
        self.horizontalLayout_4.addWidget(self.cmbScale)
        self.txtmainTitle = QtGui.QPlainTextEdit(TemplateLoader)
        self.txtmainTitle.setGeometry(QtCore.QRect(100, 90, 341, 31))
        self.txtmainTitle.setObjectName(_fromUtf8("txtmainTitle"))
        self.listViewCopyright = QtGui.QListView(TemplateLoader)
        self.listViewCopyright.setGeometry(QtCore.QRect(100, 210, 341, 83))
        self.listViewCopyright.setResizeMode(QtGui.QListView.Adjust)
        self.listViewCopyright.setObjectName(_fromUtf8("listViewCopyright"))
        self.copyright_label = QtGui.QLabel(TemplateLoader)
        self.copyright_label.setGeometry(QtCore.QRect(20, 240, 71, 21))
        self.copyright_label.setObjectName(_fromUtf8("copyright_label"))

        self.retranslateUi(TemplateLoader)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TemplateLoader.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TemplateLoader.reject)
        QtCore.QMetaObject.connectSlotsByName(TemplateLoader)
        TemplateLoader.setTabOrder(self.cmbTemplate, self.cmbScale)
        TemplateLoader.setTabOrder(self.cmbScale, self.txtmainTitle)
        TemplateLoader.setTabOrder(self.txtmainTitle, self.txtsubTitle)
        TemplateLoader.setTabOrder(self.txtsubTitle, self.iNumCarte)
        TemplateLoader.setTabOrder(self.iNumCarte, self.txtSource)
        TemplateLoader.setTabOrder(self.txtSource, self.buttonBox)

    def retranslateUi(self, TemplateLoader):
        TemplateLoader.setWindowTitle(QtGui.QApplication.translate("TemplateLoader", "Création carte", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTitle_label.setText(QtGui.QApplication.translate("TemplateLoader", "Titre", None, QtGui.QApplication.UnicodeUTF8))
        self.subTitle_label.setText(QtGui.QApplication.translate("TemplateLoader", "Sous- titre", None, QtGui.QApplication.UnicodeUTF8))
        self.txtSource_label.setText(QtGui.QApplication.translate("TemplateLoader", "Sources", None, QtGui.QApplication.UnicodeUTF8))
        self.iNumCarte_label.setText(QtGui.QApplication.translate("TemplateLoader", "Num carte", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTemplate_label.setText(QtGui.QApplication.translate("TemplateLoader", "Modèle", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbScale_label.setText(QtGui.QApplication.translate("TemplateLoader", "Echelle", None, QtGui.QApplication.UnicodeUTF8))
        self.copyright_label.setText(QtGui.QApplication.translate("TemplateLoader", "Copyright", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
