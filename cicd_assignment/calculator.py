class calculate():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        print( "addition of the numbers is ", self.a + self.b)
    
    def subtract(self):
        print("subtraction of the numbers is ", self.a - self.b)
    
    def multiply(self):
        print("Multiplication of the numbers is ", self.a * self.b)
    
    def division(self):
        if self.b == 0:
            raise ZeroDivisionError("Division by Zero is not allowed")
        else:
            print("Devision of the numbers is ", self.a / self.b)
a = float(input("enter the first number: "))
b =float(input("Enter the second number: "))
calcute = calculate(a,b)
calcute.add()
calcute.multiply()
calcute.subtract()
calcute.division()