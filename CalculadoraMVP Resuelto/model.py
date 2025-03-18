from math import log10, sqrt

# las funciones puramente de cálculo que no tienen nada que ver con el interfaz grafico
class Model(object):
    def suma(self, v1, v2):
        return v1 + v2

    def resta(self, v1, v2):
        return v1 - v2

    def mult(self, v1, v2):
        return v1 * v2

    def div(self, v1, v2):
        try:
            return v1 / v2
        except ZeroDivisionError as err:
            raise err