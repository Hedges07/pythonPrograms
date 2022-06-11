#Tyler Johnston

#user input 
num = int(input("enter a positive integer between 1 - 20 , "))

#list
L = []

#variables
index = 0

val = 1

#calculates factorial list :) 
for i in range (1, num + 1):
    val = val * i

    L.append(val)

    index = index + 1 

    num = num - 1 

#prints the values of the list accoring to the size of the list 
for j in range(len(L)):

    print(f' j = {j+1} ;\t {j+1} ! = {L[j]}')

print(f'factorial_list =    {L}')
