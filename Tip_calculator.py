# substring

#print("Hello"[4]) # or negativ indices [-1]

# premitive data types
# string = sequence of characters.
# integer = whole number

# float = floating point number

# boolean = True , False (only has 2 values)

# Type Error , Type checking , Type conversion 
# print(type(12345)) #int
# print(type("Nupoor")) #str
# print(type(3.14)) #float
# print(type(True)) #boolean


# Type conversion 
# name_of_the_user = input("Enter your name")
# length_of_name = len(name_of_the_user)

# print(type("Number of letters in you name: " )) #str
# print(type(length_of_name)) #int

# print("Number of letters in you name: " + str(length_of_name))

#Mathematical Operator

#implicit type casting

# print("My age: " + str(12))
# print(123 + 456)
# print(7 - 3)
# print(3 * 2)
# print(6 / 3)
# print(6 // 3)
# print(2**2) # exponent

#Rule of PEMDASLR left to right
# ()
# **
# * OR / 
# + OR - 

# print(3 * 3 / 3)

#round function round ()

# assigment operator
# score = 0
# score += 1
# print(score)

# f string

print("WELCOME TO THE TIP CALCULATOR")

# Get user inputs and convert them to appropriate data types
bill = float(input("What was the total bill")) #user input for total bill
tip = int(input("How much tip would you like to give ? 10 , 12 or 15 ?") )# user input for tip
split = int(input("How many people to split the bill ?")) # user input for spliting the bill

# Calculate the total tip amount and the total bill

total_amount = bill * (tip / 100) 
total_bill = bill + total_amount

## Calculate how much each person should pay
amount_per_person = total_bill / split

# Format the result to two decimal places (like currency) using f-strings

final_amount= "{:.2f}".format(amount_per_person)

# Display the results to the user

print(f"\nEach person should pay : {final_amount}")


# Breakdown of the Format Specifier {:.2f} 
# {}: This defines a placeholder within the string where the value from the .format() method will be inserted. The lack of an index (like {0}) means it automatically refers to the first argument passed to .format().
# :: This separates the field name (or index) from the format specifier itself.
# .2: This sets the precision to two, meaning it specifies the number of digits to display after the decimal point.
# f: This indicates that the value should be presented as a fixed-point floating-point number

