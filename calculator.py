
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Cannot calculate modulus by zero"
    return a % b

def power(a, b):
    return a ** b

def floor_divide(a, b):
    if b == 0:
        return "Cannot floor-divide by zero"
    return a // b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
print("Modulus:", modulus(a, b))
print("Power:", power(a, b))
print("Floor Division:", floor_divide(a, b))
