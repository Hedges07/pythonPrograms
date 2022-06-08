values = (input("Please enter a 10 digit number :"))

digits = [int(d) for d in str(values)]

print(digits)
a = sum(i for i in digits)
print(a)