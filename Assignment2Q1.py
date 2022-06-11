#Tyler Johnston

timeLimit = 20 
lowRate = 10/100
highRate = 13/100
custAreaCode = int(input("What is the area code you are calling from? "))
custPhoneNum = int(input("What is the phone number you are calling from? "))
calledAreaCode = int(input("Wgat is the area code you are calling? "))
calledPhoneNum = int(input("What is the phone number you are calling? "))
inputMinutes = int(input("In minutes, how long is the call? "))

if (custAreaCode == (calledAreaCode & (inputMinutes > timeLimit))):
    price = (inputMinutes * lowRate)
else:
     price = (inputMinutes * highRate)



print(f"The cost of calling from {custAreaCode}-{custPhoneNum} to {calledAreaCode}-{calledPhoneNum} for {inputMinutes} minutes is ${price}")