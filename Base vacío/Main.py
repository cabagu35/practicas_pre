from PyQt5 import QtWidgets
import sys
from View import View
from Presenter import Presenter
from Model import Model


class Principal(QtWidgets.QMainWindow):
    # la definicion del objeto (QtWidgets.QMainWindow) debera ser la misma que en el View
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
        app = QtWidgets.QApplication.instance()
    else:
        app = QtWidgets.QApplication(sys.argv)
    return app


if __name__ == '__main__':
    app = get_qapplication_instance()
    window = Principal()
    window.show()
    app.exec_()