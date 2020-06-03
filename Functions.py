def my_First_Function():
    print("Hello User")

my_First_Function()


def my_Second_Function(param1):
    print("Hello User " + param1)

my_Second_Function("Shane")

#  RETURN keyword - sometimes we want to retrieve some information from the function
# nothing written after the RETURN keyword in a function will be returned

def my_Third_Function_with_Return(param1):
    return param1 * param1 * param1

print(my_Third_Function_with_Return(15))

another_example = my_Third_Function_with_Return(32)
print(another_example)




