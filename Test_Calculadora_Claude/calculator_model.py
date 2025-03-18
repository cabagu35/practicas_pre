class CalculatorModel:
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset the calculator state."""
        self.current_value = 0
        self.pending_operation = None
        self.pending_operand = None
        self.new_operand = True
        self.error = None
    
    def set_operand(self, value):
        """Set the current operand."""
        try:
            self.current_value = float(value)
            self.error = None
        except ValueError:
            self.error = "Invalid input"
    
    def perform_operation(self, operation=None):
        """
        Perform the pending operation or store a new operation.
        Returns the current result.
        """
        if self.error:
            return self.current_value
        
        # If there's a pending operation, calculate the result
        if self.pending_operation and self.pending_operand is not None:
            if self.pending_operation == '+':
                self.current_value = self.pending_operand + self.current_value
            elif self.pending_operation == '-':
                self.current_value = self.pending_operand - self.current_value
            elif self.pending_operation == '*':
                self.current_value = self.pending_operand * self.current_value
            elif self.pending_operation == '/':
                if self.current_value == 0:
                    self.error = "División por cero"
                    return self.current_value
                self.current_value = self.pending_operand / self.current_value
        
        # Store the current operation for next calculation
        if operation:
            self.pending_operand = self.current_value
            self.pending_operation = operation
            self.new_operand = True
        else:
            # If operation is None (equals was pressed), reset pending operation
            self.pending_operation = None
            self.pending_operand = None
            
        return self.current_value
    
    def get_result(self):
        """Get the current calculation result."""
        if self.error:
            return self.error
        
        # Format the result to avoid unnecessary decimal places
        if self.current_value == int(self.current_value):
            return str(int(self.current_value))
        return str(self.current_value)
