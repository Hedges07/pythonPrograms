#Megan Gervais Assignment 3 Question 2

#itilize variabes given
ASSESS_PERCENT = 0.6
PROPERTY_TAX_PERCENT = 0.0072

def main():

    #itilize variables
    actualValue = 0.0

    assessValue = 0.0

    propertyTax = 0.0

    #gets actual value from user
    actualValue = float(input("Enter the actual value:"))

    #calculates the assessvalue
    assessValue = actualValue * ASSESS_PERCENT

    #calculates the propertytax
    propertyTax = assessValue * PROPERTY_TAX_PERCENT

    #calls the function that displays the values, that have been calculated 
    showPropertyTax(assessValue, propertyTax)


#prints all the values 
def showPropertyTax (assessValue, propertyTax):

    print ("Assessed value: $", format(assessValue, '.2f'))
    print ("Property tax: $", format(propertyTax, '.2f'))


main()