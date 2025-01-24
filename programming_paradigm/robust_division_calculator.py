def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        return(numerator / denominator)
    except ZeroDivisionError:
        e = "Error: Cannot divide by zero."
        return(e)
    except ValueError:
        e = "Error: Please enter numeric values only."
        return(e)
    