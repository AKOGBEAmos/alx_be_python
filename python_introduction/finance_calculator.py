# Financial Estimation Calculator

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

#Output the monthly savings
print("Your monthly savings are ${}.".format(monthly_savings))

annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Get the annual estimation
print("Projected savings after one year, with interest, is: ${}.".format(int(annual_savings)))

