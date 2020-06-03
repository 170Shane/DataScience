# Tuples are immutable - that is, they cannot be changed
# They can be thought of as a constant list
my_list = list("This is my list")
print(my_list)

my_tuple = tuple("This is my tuple")
print(my_tuple)

# We can add items to a list but cannot add items to a tuple

print("-----------------Using SORTED with TUPLES------------------")
my_sorted_tuple = sorted(my_tuple)
print("This is a sorted tuple", my_sorted_tuple)

print("-----------------Identifying Data Structure Types------------------")
print("My List is of type", type(my_list))
print("My Tuple is of type", type(my_tuple))
