#Tyler Johnston Assignment 3 Question 2

#gets input from the user 
a = input(" enter numbers, hit enter to end:")

#creates a list and adds things too it 
b = []
b.append(a) 

# while the users input is not enter, continue to take user input
while(a != ""):
    a = input("enter numbers, hit enter to end:")
    b.append(a)

#removes the last element ("") 
b.pop()

b.sort()
for x in range(len(b)):
    print(b[x])
