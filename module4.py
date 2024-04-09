class Calculator:
    brand = 'Casio MS990'

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero"

# Example usage:
my_calculator = Calculator()
result = my_calculator.add(10, 5)
print(f"Result of addition: {result}")
