# Store meals in a list
# Use a while loop to keep asking
# Use append to add to list
# Use sum to total calories

# You have meal_name, calories, meal_type collected.
# Q1: These 3 values belong to one meal — what structure holds all 3 together?
# Q2: Once you create that structure, how do you add it to meals?
# Q3: After adding, how do you ask "want to add more?" and stop if "no"?

def main():
    meals = [] # storing more meals

    while True: # using while loop to keep asking 
        meal_name = input("Enter the meal name : ")
        calories = int(input("Enter calories : "))
        meal_type = input("Enter Meal Type (breakfast/lunch/dinner) : ")
        
        meal = {'meal_name' : meal_name, 'calories':calories, 'meal_type' : meal_type}

        meals.append(meal)
        add = input("Add Another meal ? (yes/no) : ").strip().lower()
        if add == 'no':
           break


# Two things after the loop:
# Q1: How do you print each meal? (you need to loop through meals and print each one)
# Q2: How do you print total calories? (you just told me the answer 10 minutes ago)  
     
    for meal in meals:
        print(f"{meal['meal_name']}, {meal['calories']} , {meal['meal_type']}......")
        
    
    print("------Your Meal Report-------")
    total = sum(meal['calories'] for meal in meals)
    print(f" Total Calories {total}")

   # ---- Water Intake -----

    total_water = 0
    while True:
        water = int(input("Enter Water intake :"))
        total_water += water

        add = input("Add more? (yes/no): ")  
        if add == "no":
           break

    if  total_water >= 8:
        print("Well Done , Stay Hydrated !!") 
    
    elif total_water >= 5 :
        print("Drink up ")
    
    else :
        print("DRINKKKKKKKKKKKKKKKKKKK ASAPPPPPPPPP")
        


main()    