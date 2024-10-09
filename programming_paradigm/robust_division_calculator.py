# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely perform division between two numbers.
    
    Args:
        numerator (str): The numerator value (expected to be convertible to float).
        denominator (str): The denominator value (expected to be convertible to float).
    
    Returns:
        str: The result of the division or an appropriate error message.
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Attempt division
        result = num / denom
        return f"The result of the division is {result:.1f}"
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
