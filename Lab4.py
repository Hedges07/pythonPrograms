mealPrice = float(input("Enter the amount of the meal: "))
tip = round((mealPrice * .15), 2)
tax = round((mealPrice * .13) ,2) 
mealPrice = round(mealPrice+tax+tip,2)

print("Your total price is ", mealPrice)
print("Your tip was ", tip)
print("Your tax was ", tax)  
