my_list = [1, "Shane", 27.562]
# print(my_list)

# Lists are mutable in Python (can be changed)
# Lists are ORDERED COLLECTIONS

# Change an item
my_list[0] = "I have changed item 1"
# print(my_list)
#
# # Add an item
# my_list.append(True)
# print(my_list)
#
#
# # A TUPLE is an IMMUTABLE ORDERED COLLECTION
# # It can be thought of as a CONSTANT List
# my_first_tuple = (1, 5, True, "Shane Clark", "Yes")
# print(my_first_tuple)
#

# Dynamic List
# my_dynamic_list = []
# for i in range(50):
#     my_dynamic_list.append(i)
#
# print(my_dynamic_list)
#
# vowels = ["a", "e", "i", "o", "u"]
# my_distinct_list = []
# word = "This is actually a sentence, not a word"
# vowel_count = 0
# for ltr in word:
#     if ltr in vowels:
#         if ltr not in my_distinct_list:
#             my_distinct_list.append(ltr)
#         vowel_count +=1
# print("There were " + vowel_count.__str__() + " vowels in that sentence")
#
# print(my_distinct_list)

# Remove items from a list
my_list_to_remove_items_from = [1, 2, 3, 4, 5, 6, 7, "Shane", True, 19670625]
my_list_to_remove_items_from.remove(1)  # This is not the index value, this is the value that you want to be removed from the
# list and you therefore need to know the value that you want to remove
print(my_list_to_remove_items_from)

my_list_to_remove_items_from.pop()  # Pop removes the last value from a list though it does take an optional index argument to
# remove a specific value
print(my_list_to_remove_items_from)

my_list_to_remove_items_from.extend(["This", "is", "some", "extra", True, 12])  # Extend (as well as append) can also be used to
# add items to a list, including items in another list
print(my_list_to_remove_items_from)
# You can also add an empty list using append and extend - append will actually add the empty list and extend will simply ignore
# the request without an error occurring e.g. extend([]) or append([])
my_list_to_remove_items_from.append([1, 2, 3, 4, 8])
# my_list_to_remove_items_from.append(1, 2, 3, 4, 8) # Runtime error - append can only take one argument, though that are argument
# could be a list which contains multiple values
print(my_list_to_remove_items_from)

# append and extend add values to the END of an existing list
# insert takes an index value and an object and places it before the relevant index
my_list_to_remove_items_from.insert(1, "My inserted item")
print(my_list_to_remove_items_from)

my_list_to_remove_items_from.insert(0, "My inserted item at the end")  # adds an items to the start when using 0
print(my_list_to_remove_items_from)

my_list_to_remove_items_from.insert(-1, "My inserted item from the right")  # adds an item x indexes from the right
# when using negative numbers
print(my_list_to_remove_items_from)

my_list_to_remove_items_from.append(999)
print(my_list_to_remove_items_from)

my_list_to_remove_items_from.insert(-1, 998)
print(my_list_to_remove_items_from)

phrase = "Don't panic"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(3):
    plist.pop()
plist.remove("D")
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

# TODO - Continue Training
