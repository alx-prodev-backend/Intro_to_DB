# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs a basic arithmetic operation on two numbers.

    Parameters:
        num1 (float): The first number
        num2 (float): The second number
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')

    Returns:
        float or str: The result of the operation or an error message for invalid input/division by zero
    """
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        case _:
            return "Error: Invalid operation"
