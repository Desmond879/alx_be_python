# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely performs division of two numbers, handling division by zero and non-numeric input errors.
    
    Parameters:
    numerator: The numerator for the division (expected to be numeric).
    denominator: The denominator for the division (expected to be numeric).
    
    Returns:
    str: The result of the division or an error message if an exception occurs.
    """
    try:
        # Attempt to convert both numerator and denominator to float
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Check for division by zero
        if denominator == 0:
            return "Error: Cannot divide by zero."

        # Perform the division and return the result
        result = numerator / denominator
        return f"The result of the division is {result}."

    except ValueError:
        return "Error: Please enter numeric values only."

