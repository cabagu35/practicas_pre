from math import log10, sqrt

# las funciones puramente de cálculo que no tienen nada que ver con el interfaz grafico
class Model(object):
    def __init__(self):
        super().__init__()

    def log10(self, v1):
        return log10(v1)

    def cuad(self, v1):
        return v1 ** 2

    def arrel(self, v1):
        return sqrt(v1)

    def suma(self, v1, v2):
        return v1 + v2

    def resta(self, v1, v2):
        return v1 - v2

    def mult(self, v1, v2):
        return v1 * v2

    def div(self, v1, v2):
        return v1 / v2