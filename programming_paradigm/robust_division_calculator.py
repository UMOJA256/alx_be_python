# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Divides numerator by denominator safely.

    Parameters:
        numerator (any): The numerator value.
        denominator (any): The denominator value.

    Returns:
        float or str: The division result or an error message.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
