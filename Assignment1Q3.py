#Megan Gervais

a = int(input("Enter your age: "))
r = int(input("Enter your resting heart rate: "))

trainingRate = (.7*(220-a) +(.3*r))
print ("Your Training Rate(beats/min) is : ", trainingRate)
