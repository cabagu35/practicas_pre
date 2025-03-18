from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic
import os

class CalculatorView(QMainWindow):
    # Signals
    digit_clicked = pyqtSignal(str)
    operation_clicked = pyqtSignal(str)
    equals_clicked = pyqtSignal()
    clear_clicked = pyqtSignal()
    decimal_clicked = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.connect_signals()
        
    def load_ui(self):
        """Load the UI from the .ui file."""
        # Get the directory where this script is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Path to the UI file
        ui_file = os.path.join(current_dir, "calculator.ui")
        # Load the UI
        uic.loadUi(ui_file, self)
        
    def connect_signals(self):
        """Connect UI elements to signals."""
        # Connect digit buttons
        for i in range(10):
            button = getattr(self, f"button{i}")
            button.clicked.connect(lambda checked, digit=str(i): self.digit_clicked.emit(digit))
        
        # Connect operation buttons
        self.buttonAdd.clicked.connect(lambda: self.operation_clicked.emit("+"))
        self.buttonSubtract.clicked.connect(lambda: self.operation_clicked.emit("-"))
        self.buttonMultiply.clicked.connect(lambda: self.operation_clicked.emit("*"))
        self.buttonDivide.clicked.connect(lambda: self.operation_clicked.emit("/"))
        
        # Connect other buttons
        self.buttonEquals.clicked.connect(self.equals_clicked.emit)
        self.buttonClear.clicked.connect(self.clear_clicked.emit)
        self.buttonDecimal.clicked.connect(self.decimal_clicked.emit)
    
    def set_display_text(self, text):
        """Set the calculator display text."""
        self.display.setText(text)
    
    def get_display_text(self):
        """Get the current display text."""
        return self.display.text()
    
    def display_error(self, error_message):
        """Display an error message."""
        self.display.setText(error_message)
