# Simple Calculator in Python


# Function to perform calculation
def calculator():
    print("Simple Calculator")
    print("Available operation: +, -, *, /")

    # Get input from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the chosen operation
    if operation == '+':
        result = num1 + num2
        print("Result:", result)
    elif operation == '-':
        result = num1 - num2
        print("Result:", result)
    elif operation == '*':
        result = num1 * num2
        print("Result:", result)
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation.")

# Run the calculator
calculator()
    
    
