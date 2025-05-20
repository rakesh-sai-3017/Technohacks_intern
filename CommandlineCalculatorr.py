def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(" Invalid input! Please enter a number.")

def display_menu():
    print("\n *Simple Python Calculator*")
    print(" Addition (+)")
    print(" Subtraction (-)")
    print(" Multiplication (*)")
    print(" Division (/)")
    print(" Quit (q)")

def calculator():
    while True:
        display_menu()
        operation = input("\nChoose an operation (+, -, *, /) or 'q' to quit: ").strip()
        
        if operation.lower() == 'q':
            print(" Goodbye! Thanks for using the calculator.")
            break
        
        if operation not in ['+', '-', '*', '/']:
            print(" Invalid operation! Please choose +, -, *, /")
            continue
        
        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        
        print(f"\n Result: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()-
