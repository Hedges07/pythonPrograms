#Megan Gervais 
loan = int(input("Enter future value: "))
interest = float(input("Enter  interest rate (as %): "))
years = int(input("Enter  nubmber of years: "))
presentValue = loan/pow((1+(interest/100)) ,years)
presentValue = round(presentValue,2) 
print("present value: $", presentValue)