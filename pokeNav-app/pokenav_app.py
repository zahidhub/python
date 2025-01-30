import math

#THE MAIN MENU OPTION
def main_menu():
    option = ''
    while option != '1':
        display_menu()
        option = input("\nType your option: ")

        match option:
            case '1':
                print("Thank you for playing! See you next time!")
            case '2':
                identify_hashtags()
            case '3':
                detect_palindrome()
            case '4':
                create_acronym()
            case '5':
                get_pokemon_traits()
            case '6':
                match_zodiac_sign_and_element()
            case '7':
                bmi_calculator()
            case '8':
                fitness_and_health_tracker()
            case _:
                print("Error - Invalid option. Please input a number between 1 and 8.")

#IDENTIFY HASHTAGS
def identify_hashtags():
    post_elements = input("Type your post: ").lower().split()
    hashtags = []
    unique_hashtags = []

    for element in post_elements:
        if element.startswith("#"):
            hashtags.append(element)

    for item in hashtags:
        if item not in unique_hashtags:
            unique_hashtags.append(item)

    if unique_hashtags:
        print("Hashtags found:")
        for item in unique_hashtags:
            print(item)
    else:
        print("No hashtags found.")

#IDENTIFY PALINDROME TASK
def detect_palindrome():
    pokemon_name = input("Type your pokemon name: ")
    #Comparing the name while lowercased, due to the name being case sensitive
    if pokemon_name.lower() == pokemon_name[::-1].lower(): 
        print(f"The name '{pokemon_name}' is a palindrome.")
    else:
        print(f"The name '{pokemon_name}' is not a palindrome.")

#CREATE ACRONYM FROM TASK
def create_acronym():
    pokemon_name = input("Type your pokemon name: ").lower()
    shortening_factor = int(input("Type your shortening factor: "))
    acronym = ""

    for i in range(shortening_factor-1, len(pokemon_name), shortening_factor):
        acronym += pokemon_name[i]
    print(f"Abbreviated name: {acronym.upper()}")

#FIND POKEMON TRAITS
def get_pokemon_traits():
    pokemon_name = input("Type your pokemon name: ")
    pokemon_type = input("Type your Pokemon type: ").lower()

    if pokemon_type == "fire":
        print(f"{pokemon_name} is a Fire-type Pokemon! It is strong against Grass-type Pokemons and weak against Water-type Pokemons.")
    elif pokemon_type == "water":
        print(f"{pokemon_name} is a Water-type Pokemon! It is strong against Fire-type Pokemons and weak against Grass-type Pokemons.")
    elif pokemon_type == "grass":
        print(f"{pokemon_name} is a Grass-type Pokemon! It is strong against Water-type Pokemons and weak against Fire-type Pokemons.")
    else:
        print("Error - The Pokemon type provided is not valid. Valid types: Water, Fire, Grass.")

#FIND ZODIAXC SIGN AND EEVEELUTION TASK
def match_zodiac_sign_and_element():

     #List of zodiac signs (corresponding to months)
    zodiac_signs = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini",
                    "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]

    birth_month = int(input("Type your birth month: "))

    if not (1 <= birth_month <= 12):
        print("Error - The month index provided is not valid. Choose between 1 and 12.")
        return
    
    #Matches birth month to corresponding zodiac sign
    zodiac_sign = zodiac_signs[birth_month - 1]

    #Finds the zodiac element and eeveelution based on the zodiac sign
    if zodiac_sign in ["Cancer", "Scorpio", "Pisces"]:
        element = "Water"
        eeveelution = "Vaporeon"
    elif zodiac_sign in ["Aries", "Leo", "Sagittarius"]:
        element = "Fire"
        eeveelution = "Flareon"
    elif zodiac_sign in ["Taurus", "Virgo", "Capricorn"]:
        element = "Earth"
        eeveelution = "Leafeon"
    else:
        element = "Air"
        eeveelution = "Jolteon"
            
    print(f"""
    Zodiac Sign: {zodiac_sign}
    Element: {element}
    Eeveelution: {eeveelution}""")

#CALCULATE POKEMON BMI TASK
def bmi_calculator():

    height = float(input("Please enter your Pokemon's height in meters: "))
    weight = float(input("Please enter your Pokemon's weight in kilograms: "))

    if height <= 0 and weight <= 0:
        print("Error - Height and weight must be positive numbers.")
        return
    elif height <= 0:
        print("Error - Height must be a positive number.")
        return
    elif weight <= 0:
        print("Error - Weight must be a positive number.")
        return
    
    bmi = weight / (height ** 2) #Calculates BMI
    bmi_rounded = round(bmi, 2) #Rounds calculated BMI to two decimal places


    #Finds weight category based on the rounded BMI
    if bmi_rounded < 29:
        category = "underweight"
    elif 29 <= bmi_rounded < 53:
        category = "healthy"
    elif 53 <= bmi_rounded < 85:
        category = "overweight"
    else:
        category = "obese"

    print (f"BMI = {bmi_rounded:.2f}. The Pokemon is {category}. ")

#FITNESS AND HEALTH TRACKING TASK
def fitness_and_health_tracker():

    #List of the days of the week, needed for output
    week_day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] 
    steps_input = input ("Please enter steps counted per day, starting from Sunday and with each day separated by a comma: ")

    DAY_COUNT = 7

    #Splits the user's input string by commas (and converts each separated string into an integer)
    steps = []
    for step_count in steps_input.split(','):
        step_count = step_count.strip() #Remove any empty or invalid input
        if step_count:  #Check if the string is empty
            steps.append(int(step_count)) #Add the value into steps after converting to integer

    if len(steps) != DAY_COUNT:
        print(f"Error - Invalid input. The program needs 7 numbers; you typed {len(steps)} numbers.")
        return

    total_steps = sum(steps) #Counts the total amount of steps for the week
    average_steps = total_steps/DAY_COUNT #Calculates average steps per day

    #Adds up the squared the differences from the average
    variance = sum ((each_step - average_steps) ** 2 for each_step in steps) 
    std_steps = math.sqrt(variance/DAY_COUNT) #Calculates standard deviation
    
    #Finds the most active day of the week (by the index), and chooses the later day if there is 2 identical numbers
    most_active_day = max(range(len(steps)), key=lambda day_index: (steps [day_index], day_index))
    #Find the least active day of the week (by the index), and chooses the later day if there is 2 identical numbers
    least_active_day = min(range(len(steps)), key=lambda day_index: (steps [day_index], -day_index))

    #Prints steps statistics (rounded to two decimal places)
    print(f"Steps Statistics:{average_steps: .2f} + / - {std_steps:.2f} per day.")
    #Prints the most and the least active days
    print(f"Most active day: {week_day[most_active_day]}. Least active day: {week_day[least_active_day]}.")

#MENU TEXT
def display_menu():
    print(f"""
    Welcome to the Main Menu. Choose one of the options below:
        1. Exit
        2. Identify hashtags
        3. Detect a palindrome
        4. Create an acronym
        5. Get Pokemon traits
        6. Match zodiac sign and element
        7. BMI calculator
        8. Fitness and health tracker """)

#RUN METHOD
if __name__ == "__main__":
    main_menu()
