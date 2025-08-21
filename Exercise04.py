
def add (x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

while True:
    print("\nEnter operation (+, -, *, /) or exit:")
    op = input("Operation: ")

    if op == "exit":
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if op == "+":
        print("Result:", add(num1, num2))
    elif op == "-":
        print("Result:", subtract(num1, num2))
    elif op == "*":
        print("Result:", multiply(num1, num2))
    elif op == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation")



