# -*- coding: utf-8 -*-
# Base PyQt5
import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow,QApplication, QMessageBox
 # Cargar nuestro formulario *.ui
form_class = uic.loadUiType("calculadora.ui")[0]
#Crear la Clase MyWindowClass con el formulario cargado.
class MyWindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
 #Implementacion de los Slots referenciados en QDesigner

    def entrada(self):
        try:
            v1 = float(self.entrada1.text())
            v2 = float(self.entrada2.text())
            return v1, v2
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Valor no válido')

    def salida(self, res):
        # mostrar en el contenedor del resultado
        self.etresultado.setText('0.3f' % res)
        
    def suma(self):
        x, y = self.entrada()
        s = x + y
        self.salida(s)
    
    def resta(self):
        x, y = self.entrada()
        s = x - y
        self.salida(s)
        
    def multiplicacion(self):
        x, y = self.entrada()
        s = x * y
        self.salida(s)
        
    def division(self):
        x, y = self.entrada()
        try:
            s = x / y
            self.salida(s)
        except ZeroDivisionError:
            QMessageBox.warning(self, 'Error' , 'Error división por cero')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()
