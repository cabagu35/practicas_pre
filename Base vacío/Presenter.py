# Aqui esta el codigo que conecta View con Model
from PyQt5.QtWidgets import QMessageBox

class Presenter(object):
    # Pasar el View y el Model dentro del Presenter
    def __init__(self, view,model):
        self.vista = view
        self.modelo = model
        #captura de las señales del View y conectando con funciones del Presenter
        self.vista.btnsuma.connect(self.fsuma)
        self.vista.btnresta.connect(self.fresta)
        self.vista.btnmulti.connect(self.multi)
        self.vista.btndivi.connect(self.divi)


    # Funciones del Presenter
    def fsuma(self):
        v1, v2 = self.vista.entrada()
        r = self.modelo.suma(v1, v2)
        self.vista.salida(r)

    def fresta(self):
        v1, v2 = self.vista.entrada()
        r = self.modelo.resta(v1, v2)
        self.vista.salida(r)

    def multi(self):
        v1, v2 = self.vista.entrada()
        r = self.modelo.multi(v1, v2)
        self.vista.salida(r)

    def divi(self):
        try:
            v1, v2 = self.vista.entrada()
            r = self.modelo.divi(v1, v2)
            self.vista.salida(r)
        except ZeroDivisionError:
            QMessageBox.warning(self.vista, 'Error', 'No se puede dividir por cero')
        

