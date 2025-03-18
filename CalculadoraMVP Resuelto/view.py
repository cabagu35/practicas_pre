from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui_CalculadoraV2 import Ui_Calculadora as form_class
import sys


class View(QtWidgets.QMainWindow, form_class):
    # la definicion del objeto (QtWidgets.QMainWindow) debera ser la misma que en el Main
    # crear los signals para enviarlos al Presenter
    btnsuma = QtCore.pyqtSignal()
    btnresta = QtCore.pyqtSignal()
    btnmulti = QtCore.pyqtSignal()
    btndivi = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        # icicializamos el formulario poniendo los componentes a los valores iniciales.
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # poner componentes a su valor inicial
        self.desctivabotones()

    # Implementacion de slots
    def verifica(self):
        try:
            _ = float(self.entrada1.text())
            _ = float(self.entrada2.text())
            self.activabotones()
        except:
            self.desctivabotones()

    def desctivabotones(self):
        self.btsuma.setEnabled(False)
        self.btresta.setEnabled(False)
        self.btmulti.setEnabled(False)
        self.btdivi.setEnabled(False)

    def entrada(self):
        a = float(self.entrada1.text())
        b = float(self.entrada2.text())
        return a, b

    def salida(self, valor):
        self.resultado.setText("%0.3f" % (valor))

    def mensaje(self, prompt, txt):
        QMessageBox.critical(prompt, txt)

    def activabotones(self):
        self.btsuma.setEnabled(True)
        self.btresta.setEnabled(True)
        self.btmulti.setEnabled(True)
        self.btdivi.setEnabled(True)

    def opera(self):
        boton = self.sender()
        op = boton.text()
        if op == '+':
            self.btnsuma.emit()
        elif op == '-':
            self.btnresta.emit()
        elif op == '*':
            self.btnmulti.emit()
        elif op == '/':
            try:
                self.btndivi.emit()
            except ZeroDivisionError as err:
                self.mensaje('error', str(err))

    def close(self):
        reply = QMessageBox.question(self, 'Confirmar cierre',
                                     '¿Estás seguro de que quieres cerrar la ventana?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # super().close()
            sys.exit()
