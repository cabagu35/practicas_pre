import sys

from PyQt5 import QtWidgets

from model import Model
from presenter import Presenter
from view import View


class Calculadora(QtWidgets.QMainWindow):
    # la definición del objeto (QtWidgets.QMainWindow) debera ser la misma que en el View
    def __init__(self, parent=None):
        super().__init__(parent)

        self.window = QtWidgets.QMainWindow()
        self.my_view = View()
        self.my_model = Model()
        self.my_presenter = Presenter(self.my_view, self.my_model)
        self.setCentralWidget(self.my_view)
        self.setWindowTitle("Calculadora")


def get_qapplication_instance():
    if QtWidgets.QApplication.instance():
        apk = QtWidgets.QApplication.instance()
    else:
        apk = QtWidgets.QApplication(sys.argv)
    return apk


if __name__ == '__main__':
    app = get_qapplication_instance()
    window = Calculadora()
    window.resize(530, 170)
    window.show()
    app.exec_()
