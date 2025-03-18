from PyQt5 import QtCore,QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from ui_CalculadoraV2 import Ui_Calculadora as form_class


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
        self.desactivabotones()
        self.entrada1.setText('')
        self.entrada2.setText('')
        self.etresultado.setText('')
    

    def entrada(self):
        try:
            a = float(self.entrada1.text())
            b = float(self.entrada2.text())
            return a, b
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Valor no válido')
    
    def salida(self, res):
        # mostrar en el contenedor del resultado
        self.etresultado.setText('0.3f' % res)
    
    def opera(self, res):
        boton = self.sender


        


    # definicion de los slots
    def Slot1(self):
        # gestion de errores del view
        try:
            # XXXXX
            self.btnXXXXX.emit() # se emite la señal para el presenter
        except ValueError:
            QMessageBox.information(self, 'Error', 'Texto')