#Tyler Johnston
A = float(input("Enter amount of loan: "))
r = float(input("Enter interest rate: "))
n = float(input("Enter nubmber of years: "))
i = r / 1200 
monthlyPayment = A*(i/(1 - pow((1 + i), -12*n)))
monthlyPayment = round(monthlyPayment,2)
print("Monthly Payment : $", +monthlyPayment)
