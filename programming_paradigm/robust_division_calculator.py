def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        answer = numerator / denominator
        result = f"The result of the division is {answer:.1f}"
        return(result)
    except ZeroDivisionError:
        e = "Error: Cannot divide by zero."
        return(e)
    except ValueError:
        e = "Error: Please enter numeric values only."
        return(e)
    