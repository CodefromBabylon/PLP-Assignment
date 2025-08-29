def calculator():
    """A basic calculator function that performs operations on two numbers."""
    
    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return
    
    # Perform the calculation based on the operation
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Error: Invalid operation. Please use +, -, *, or /.")
        return
    
    # Display the result
    print(f"{num1} {operation} {num2} = {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()