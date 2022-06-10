#itilize variabes given
caloriesFromFat = 9
CaloriesFromCarbs = 4

def main(): 

    #itilize variables
    gramsFat = 0.0

    gramsCarbs = 0.0

    caloriesFat = 0.0

    caloriesCarbs = 0.0


    #gets the values from the users 
    gramsFat = float(input("Enter fat grams consumed:"))
    gramsCarbs = float(input("Enter carbohydrate grams consumed:"))

    #calculates the calories 
    caloriesFat = (gramsFat * caloriesFromFat)

    #calculates the carbs
    caloriesCarbs = (gramsCarbs * CaloriesFromCarbs)

    #disaplay the values 
    display(gramsFat, gramsCarbs, caloriesFat, caloriesCarbs)

#Function that displays the values 
def display(gramsFat, gramsCarbs, caloriesFat, caloriesCarbs):

    print(f'Grams of fat: {gramsFat}')
    print(f'Result Calories: {caloriesFat}')
    print(f'Grams of carbs: {gramsCarbs}')
    print(f'Result Calories: {caloriesCarbs}')

main()
