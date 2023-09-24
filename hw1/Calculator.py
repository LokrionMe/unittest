class Calculator:
    def __init__(self):
        pass

    def add(self, x1, x2):
        return x1 + x2

    def multiply(self, x1, x2):
        return x1 * x2

    def subtract(self, x1, x2):
        return x1 - x2

    def divide(self, x1, x2):
        if x2 != 0:
            return x1/x2

    def discount(self, price, disc):
        if disc < 100:
            return price * (100 - disc) / 100
        return ArithmeticError("Discount must be less than 100")
    