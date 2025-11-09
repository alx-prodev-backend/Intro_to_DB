# user_income = int(input("Enter your monthly income:"))
# total_monthly_expenses = int(input("Enter your total monthly expenses:"))
# monthly_savings = float(user_income - total_monthly_expenses)
# projected_savings = float(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
#
# print(f"Your monthly savings are ${monthly_savings}.")
# print(f"Projected savings after one year, with interest, is:  ${projected_savings}.")
#

# finance_calculator.py 💰
# Calculates monthly and projected annual savings

# Get user input
user_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = user_income - total_monthly_expenses

# Project annual savings with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display results
print(f"\nYour monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
