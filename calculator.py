#simple calculator app

operation = input("+ , - , * , / ")
num1 = float(input("enter 1st number:"))
num2 = float(input("enter 2nd number:"))

if operation == "+":
    result = num1 + num2
    print(round(result,3))
elif operation == "-":
    result = num1 - num2
    print(round(result,3))   
elif operation == "*":
    result = num1 * num2
    print(round(result,3))       
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(round(result,3))
    else:
        print("Error: Division by zero is not allowed.")    
else:
    print(f"{operation} is not a valid operator")          