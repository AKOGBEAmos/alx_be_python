# Interactive calculator

print("---- The calculator is ON & READY ----")
choice = 1
while choice == 1:
    num1 =  int(input("Enter the first number: "))
    num2 =  int(input("Enter the second number: "))

    #Choose the operation
    operation = input("Choose the operation (+, -, *, /): ")
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        case "*":
            result = num1* num2
            print(f"The result is {result}.")
        case "/":
            #Handle ZeroDivisionError
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1/num2
                print(f"The result is {result}.")
    print("---- The calculator is ON & READY ----")
    choice = int(input("Do you want to perform another operator (1-Yes | 0 -No) "))