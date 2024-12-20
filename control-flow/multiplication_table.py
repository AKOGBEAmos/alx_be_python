# Multiplication Table

choice = 1
while choice == 1:
    print("+++++++ Multiplication Table +++++++")
    print("Rules: The number must be an integer.")
    number = int(input("Enter a number to see its multiplication table:"))

    #Generate the table
    for x in range(1,11):
        print(f"{number} * {x} = {number * x}")
    
    print("\n")    
    print("+++++++ Multiplication Table +++++++")
    choice = int(input(("Do you want another table? (Yes--->1 |  No--->0) ")))