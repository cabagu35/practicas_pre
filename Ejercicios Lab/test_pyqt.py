from PyQt5.QtWidgets import (QApplication, QDialog, QFormLayout, QPushButton, QVBoxLayout)

import sys

class Dialog(QDialog):
    def slot_method(self):
        print('Llamada al metodo Slot.')
    def __init__(self):
        super(Dialog, self).__init__()
        button=QPushButton("Click")
        button.clicked.connect(self.slot_method)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)
        self.setLayout(mainLayout)
        self.setGeometry(800,600,100,50)
        self.setWindowTitle("Ejemplo Botón")


if __name__ == '__main__':
 app = QApplication(sys.argv)
 dialog = Dialog()
 sys.exit(dialog.exec_())