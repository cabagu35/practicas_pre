# -*- coding: utf-8 -*-
# Base PyQt5
import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow,QApplication
 # Cargar nuestro formulario *.ui
form_class = uic.loadUiType("MiFormulario.ui")[0]
#Crear la Clase MyWindowClass con el formulario cargado.
class MyWindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
 #Implementacion de los Slots referenciados en QDesigner
    def xxxx(self):
        pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()
