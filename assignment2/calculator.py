def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

num1 = int(input("Enter value of a: "))
num2 = int(input("Enter value of b: "))
op = input("Enter operator (+, -, *, /): ")
if op == "+":
    print(f"Sum of {num1} + {num2} is :", add(num1, num2))
elif op == "-":
    print(f"Substraction of {num1} - {num2} is :", sub(num1, num2))
elif op == "*":
    print(f"Multiplication of {num1} * {num2} is :", mul(num1, num2))
elif op == "/":
    print(f"Division of {num1} / {num2} is :", div(num1, num2))
else:
    print("Invalid operator.")