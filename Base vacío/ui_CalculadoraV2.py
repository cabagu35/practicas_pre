# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalculadoraV2XDTgri.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_Calculadora(object):
    def setupUi(self, Calculadora):
        if Calculadora.objectName():
            Calculadora.setObjectName(u"Calculadora")
        Calculadora.resize(531, 193)
        self.splitter_6 = QSplitter(Calculadora)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setGeometry(QRect(40, 20, 441, 131))
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.splitter = QSplitter(self.splitter_6)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.entrada2 = QLineEdit(self.splitter)
        self.entrada2.setObjectName(u"entrada2")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(22)
        self.entrada2.setFont(font)
        self.splitter.addWidget(self.entrada2)
        self.entrada1 = QLineEdit(self.splitter)
        self.entrada1.setObjectName(u"entrada1")
        self.entrada1.setFont(font)
        self.splitter.addWidget(self.entrada1)
        self.resultado = QLabel(self.splitter)
        self.resultado.setObjectName(u"resultado")
        self.resultado.setMinimumSize(QSize(181, 30))
        self.resultado.setFont(font)
        self.splitter.addWidget(self.resultado)
        self.splitter_6.addWidget(self.splitter)
        self.splitter_5 = QSplitter(self.splitter_6)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Vertical)
        self.splitter_4 = QSplitter(self.splitter_5)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.splitter_2 = QSplitter(self.splitter_4)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.btsuma = QPushButton(self.splitter_2)
        self.btsuma.setObjectName(u"btsuma")
        self.btsuma.setMinimumSize(QSize(80, 30))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.btsuma.setFont(font1)
        self.splitter_2.addWidget(self.btsuma)
        self.btresta = QPushButton(self.splitter_2)
        self.btresta.setObjectName(u"btresta")
        self.btresta.setMinimumSize(QSize(80, 30))
        self.btresta.setFont(font1)
        self.splitter_2.addWidget(self.btresta)
        self.splitter_4.addWidget(self.splitter_2)
        self.splitter_3 = QSplitter(self.splitter_4)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.btmulti = QPushButton(self.splitter_3)
        self.btmulti.setObjectName(u"btmulti")
        self.btmulti.setMinimumSize(QSize(80, 30))
        self.btmulti.setFont(font1)
        self.splitter_3.addWidget(self.btmulti)
        self.btdivi = QPushButton(self.splitter_3)
        self.btdivi.setObjectName(u"btdivi")
        self.btdivi.setMinimumSize(QSize(80, 30))
        self.btdivi.setFont(font1)
        self.splitter_3.addWidget(self.btdivi)
        self.splitter_4.addWidget(self.splitter_3)
        self.splitter_5.addWidget(self.splitter_4)
        self.btsalida = QPushButton(self.splitter_5)
        self.btsalida.setObjectName(u"btsalida")
        self.btsalida.setMinimumSize(QSize(80, 30))
        self.splitter_5.addWidget(self.btsalida)
        self.splitter_6.addWidget(self.splitter_5)

        self.retranslateUi(Calculadora)
        self.btsuma.clicked.connect(Calculadora.opera)
        self.btsalida.clicked.connect(Calculadora.close)
        self.btresta.clicked.connect(Calculadora.opera)
        self.btmulti.clicked.connect(Calculadora.opera)
        self.btdivi.clicked.connect(Calculadora.opera)
        self.entrada1.textChanged.connect(Calculadora.verifica)
        self.entrada2.textChanged.connect(Calculadora.verifica)

        QMetaObject.connectSlotsByName(Calculadora)
    # setupUi

    def retranslateUi(self, Calculadora):
        Calculadora.setWindowTitle(QCoreApplication.translate("Calculadora", u"Cuadro", None))
        self.entrada1.setText("")
        self.resultado.setText("")
        self.btsuma.setText(QCoreApplication.translate("Calculadora", u"+", None))
        self.btresta.setText(QCoreApplication.translate("Calculadora", u"-", None))
        self.btmulti.setText(QCoreApplication.translate("Calculadora", u"*", None))
        self.btdivi.setText(QCoreApplication.translate("Calculadora", u"/", None))
        self.btsalida.setText(QCoreApplication.translate("Calculadora", u"salir", None))
    # retranslateUi

