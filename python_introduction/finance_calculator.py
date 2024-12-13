# Financial Estimation Calculator

income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

savings = income - expenses

#Output the monthly savings
print("Your monthly savings are ${}.".format(savings))

annual_savings = savings * 12 + (savings * 12 * 0.05)

#Get the annual estimation
print("Projected savings after one year, with interest, is: ${}.".format(int(annual_savings)))

