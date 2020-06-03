# Python's for Loop understands lists
# It knows where the list starts, where it ends and how many objects the list contains

my_new_list = list("It knows where the list starts, where it ends and how many objects the list contains")
print(my_new_list)

for my_variable in my_new_list:
    print('\t', '\t', '*' * 3, my_variable)  # Just messing about '\t' is a Tab character which is also printed
