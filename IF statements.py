is_male = False

if is_male:
    print("Is a male!")
elif not is_male:
    print("something")
else :
    print("Is a female!")

# using comparisons in if statements
# create a function to return the maximum value of three parameters
def return_maximum_number(param1, param2, param3):
    return max(param1, param2, param3)

result = return_maximum_number(12,50,987)
print(result)


def return_maximum_mumber_alternative(param1, param2, param3):
    if param1 >= param2 and param1 >= param3:
        return param1
    elif param2 >= param1 and param2 >= param3:
        return  param2
    else:
        return param3

result_alternative = str(return_maximum_mumber_alternative(27,245,96)) + " is the highest number"
print(result_alternative)

# a better calculator
num1 = float(input("Please enter your first number : "))
num2 = float(input("Please enter your second number : "))
calculation = input("Please enter a calculation using /, * , + or - : ")

def calculator(param1, param2, param3):
    if param3 == "*":
        return  param1 * param2
    elif param3 == "-":
        return  param1 - param2
    elif param3 == "+":
        return  param1 + param2
    elif param3 == "/":
        return  param1 / param2
    else:
        print("Invalid Operator")

results_new_calculator = calculator(num1,num2,calculation)
print("The result is " + str(results_new_calculator))