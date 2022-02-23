# Tip Calculator
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places = 33.60

print("Welcome to Tip Calculator")
bill = float(input("What was the total bill? $"))
people = int(input("How many people will split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill_with_tip = bill + bill * (tip_percentage / 100)
each_person_bill = round(bill_with_tip / 5, 2)
each_person_bill_as_string = "{:.2f}".format(each_person_bill)
print(f"Each person should pay: ${each_person_bill_as_string}")
