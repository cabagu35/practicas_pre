from calculator_model import CalculatorModel
from calculator_view import CalculatorView

class CalculatorPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        # Connect view signals to presenter methods
        self.view.digit_clicked.connect(self.on_digit_clicked)
        self.view.operation_clicked.connect(self.on_operation_clicked)
        self.view.equals_clicked.connect(self.on_equals_clicked)
        self.view.clear_clicked.connect(self.on_clear_clicked)
        self.view.decimal_clicked.connect(self.on_decimal_clicked)
        
        # Initialize display
        self.new_operand = True
    
    def on_digit_clicked(self, digit):
        """Handle digit button clicks."""
        current_text = self.view.get_display_text()
        
        # Start a new operand or append to the current one
        if current_text == "0" or self.new_operand or current_text == "Error":
            self.view.set_display_text(digit)
            self.new_operand = False
        else:
            self.view.set_display_text(current_text + digit)
    
    def on_decimal_clicked(self):
        """Handle decimal point button click."""
        current_text = self.view.get_display_text()
        
        # Start a new operand with decimal point
        if self.new_operand:
            self.view.set_display_text("0.")
            self.new_operand = False
        # Add decimal point if not already present
        elif "." not in current_text:
            self.view.set_display_text(current_text + ".")
    
    def on_operation_clicked(self, operation):
        """Handle operation button clicks."""
        # First, process the current value on display
        current_text = self.view.get_display_text()
        if current_text != "Error":
            self.model.set_operand(current_text)
            
            # Perform the operation and display the result
            result = self.model.perform_operation(operation)
            
            if self.model.error:
                self.view.display_error(self.model.error)
            else:
                self.view.set_display_text(self.model.get_result())
            
            self.new_operand = True
    
    def on_equals_clicked(self):
        """Handle equals button click."""
        current_text = self.view.get_display_text()
        if current_text != "Error":
            self.model.set_operand(current_text)
            
            # Perform the final calculation and display the result
            result = self.model.perform_operation()
            
            if self.model.error:
                self.view.display_error(self.model.error)
            else:
                self.view.set_display_text(self.model.get_result())
            
            self.new_operand = True
    
    def on_clear_clicked(self):
        """Handle clear button click."""
        self.model.reset()
        self.view.set_display_text("0")
        self.new_operand = True


# Main application entry point
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from calculator_model import CalculatorModel
    from calculator_view import CalculatorView
    
    app = QApplication(sys.argv)
    
    # Create MVC components
    model = CalculatorModel()
    view = CalculatorView()
    presenter = CalculatorPresenter(model, view)
    
    # Show the calculator
    view.show()
    
    sys.exit(app.exec_())
