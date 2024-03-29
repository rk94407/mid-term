import sys
from decimal import Decimal, InvalidOperation
from decimal import Decimal, DivisionByZero

class OperationPlugin:
    def __init__(self):
        self.operations = {}

    def register_operation(self, operation_name, function):
        self.operations[operation_name] = function

    def execute_operation(self, operation_name, a, b):
        if operation_name in self.operations:
            return self.operations[operation_name](a, b)
        else:
            raise ValueError(f"Unknown operation: {operation_name}")

# Instantiate the plugin manager
operation_plugin = OperationPlugin()

# Define operation functions
def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise DivisionByZero("Division by zero is not allowed.")
    return a / b

# Register operations with the plugin manager
operation_plugin.register_operation("add", add)
operation_plugin.register_operation("subtract", subtract)
operation_plugin.register_operation("multiply", multiply)
operation_plugin.register_operation("divide", divide)

# Assume operation_plugin is imported from the module where it's defined

def calculate_and_print(a, b, operation_name):
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_plugin.execute_operation(operation_name, a_decimal, b_decimal)
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
    except InvalidOperation:
        print("Invalid number input: one of the inputs is not a valid number.")
    except DivisionByZero:
        print("Error: Division by zero.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function and the rest of the application remain the same


def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation_name = sys.argv
    calculate_and_print(a, b, operation_name)

if __name__ == '__main__':
    main()
