#Figure pattern drawing

size = int(input("Enter the size of the pattern: "))
x = 0
while x < size:
    for y in range(size):
        if y == size -1:
            print("*\n")
        else:
            print("*", end="")
    x+=1