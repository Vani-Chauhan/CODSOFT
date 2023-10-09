def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        operation = input("Enter operation(1/2/3/4): ")
        if operation in ('1', '2', '3', '4'):
            break
        else:
            print("Invalid input. Please enter a valid operation.")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '1':
        result = add(num1, num2)
    elif operation == '2':
        result = subtract(num1, num2)
    elif operation == '3':
        result = multiply(num1, num2)
    elif operation == '4':
        result = divide(num1, num2)

    print(f"Result: {result}")

calculator()