#Tyler Hedges-Johnston
#25402346   
#Programming for beginners Assignment 1 

a = int(input("Enter your age: "))
r = int(input("Enter your resting heart rate: "))

trainingRate = (.7*(220-a) +(.3*r))
print("Your Training Rate is: ", trainingRate)
