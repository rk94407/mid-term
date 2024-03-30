import logging
import os
import pandas as pd

# from utils import setup_logger
# logger = setup_logger()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Now you can use the logger throughout your code
logger.info("Calculator application started.")


class Calculator:
    def __init__(self):
        self.history_file = os.getenv('CALCULATOR_HISTORY_FILE', 'calculator_history.csv')
        self.precision = int(os.getenv('CALCULATOR_PRECISION', 2))
        self._load_history()

    def add(self, a, b):
        result = round(a + b, self.precision)
        self._update_history(f"{a} + {b}", result)
        return result

    def subtract(self, a, b):
        result = round(a - b, self.precision)
        self._update_history(f"{a} - {b}", result)
        return result

    def multiply(self, a, b):
        result = round(a * b, self.precision)
        self._update_history(f"{a} * {b}", result)
        return result

    def divide(self, a, b):
        if b == 0:
            logger.error("Cannot divide by zero")
            raise ValueError("Cannot divide by zero")
        result = round(a / b, self.precision)
        self._update_history(f"{a} / {b}", result)
        return result

    def _update_history(self, expression, result):
        new_entry = {'Expression': expression, 'Result': result}
        self.history = self.history._append(new_entry, ignore_index=True)
        self.history.to_csv(self.history_file, index=False)
        logger.info(f"Calculation: {expression} = {result}")
    
    def _load_history(self):
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file)
        else:
            self.history = pd.DataFrame(columns=['Expression', 'Result'])

    def clear_history(self):
        self.history = pd.DataFrame(columns=['Expression', 'Result'])
        self.history.to_csv(self.history_file, index=False)
        logger.info("Calculation history cleared")

def main():
    calculator = Calculator()
    while True:
        print("Available operations: add, subtract, multiply, divide, clear_history, exit")
        operation = input("Enter operation: ").strip().lower()
        if operation == 'exit':
            break
        elif operation == 'clear_history':
            calculator.clear_history()
        elif hasattr(calculator, operation):
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = getattr(calculator, operation)(a, b)
                print("Result:", result)
            except ValueError as e:
                logger.error(f"Invalid input: {e}")
                print("Invalid input, please try again.")
        else:
            print("Invalid operation, please try again.")

if __name__ == "__main__":
    main()
