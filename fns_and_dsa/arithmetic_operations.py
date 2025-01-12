def perform_operation(num1, num2, operation):
    if operation == 'add':
        return (num1 + num2)
    elif operation == 'substract':
        return (num1 - num2)
    elif operation == 'multiply':
        return (num1 * num2)
    elif operation == 'divide':
        try:
            return(num1 / num2)
        #Managing ZeroDivisionError
        except ZeroDivisionError as e:
            print(f"Sorry you enter 0 as value for the divider that causes the {e}")
