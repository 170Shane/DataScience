# Dictionaries are data structures in Python where the data is stored on key/value pairs e.g.
person_dictionary = {
    'Name': 'Ford Prefect',
    'Gender': 'Male',
    'Occupation': 'Researcher',
    'Home Planet': 'Ford Mercury'
}
# Dictionaries are created using curly braces notation {}

print(person_dictionary)  # print out the entire dictionary
print(person_dictionary["Name"])  # print out an item from the dictionary
# print(person_dictionary["Ford Prefect"])  # print out an item from the dictionary that isn't there = error

# The following is a loop that prints out all KEY values
for x in person_dictionary:
    print(x)
print("---------------------------------------------------------------")
# The following prints out all VALUES in the dictionary
print(person_dictionary.values())
print("---------------------------------------------------------------")

print("-----The following prints out all KEY values and actual VALUES in the dictionary-----")
# The following prints out all KEY values and actual VALUES in the dictionary
print(person_dictionary.items())
print("---------------------------------------------------------------")
# The following removes an item from the dictionary (POP method with Key Name)
print(person_dictionary.pop("Name"))
print(person_dictionary)  # print out the entire dictionary

# Can also use numbers as keys and mix data types for keys
person_dictionary2 = {
    1: 'Ford Prefect',
    2: 'Male',
    3: 'Researcher',
    "4": 'Ford Mercury'
}
print(person_dictionary2[3])
print(person_dictionary2["4"])
# Dictionaries are not necessarily stored in the same order that the records are created in. They are UNORDERED.
print("---------------------------------------------------------------")
# Adding or reassigning/updating an item to the dictionary
person_dictionary2["My_New_Value"] = "iPhone 11 Pro Max"  # Adds if Key doesn't exist
print(person_dictionary2)
person_dictionary2[1] = "iPhone 11 Pro Max now in position 1"  # Updates in Key exists
print(person_dictionary2)
print("-----------------Exercise------------------")
# Initialise a new dictionary
dictionary_found_items = {}
print(dictionary_found_items)

# Initialise some values in our new dictionary
# dictionary_found_items["a"] = 0
# dictionary_found_items["e"] = 0
# dictionary_found_items["i"] = 0
# dictionary_found_items["o"] = 0
# dictionary_found_items["u"] = 0
# dictionary_found_items["z"] = 0
print(dictionary_found_items)

# Print out all keys and values in the new dictionary NB the sorted function ensures that the results are ordered
# Note we can also use the reverse parameter to reverse the sort order
for key_value_pairs in sorted(dictionary_found_items, reverse=False):
    print(key_value_pairs, "was found", dictionary_found_items[key_value_pairs], "times")

print("---------------------------------------------------------------")

# Another way of achieving the same results is by using the ITEMS method (this is a method for dictionaries)
# This is the preferred/normal way of iterating over a dictionary as it provides access to both the key and value in the loop
for key, value in sorted(dictionary_found_items.items(), reverse=True):
    print(key, "was found", value, "times")

vowels = ["a", "e", "i", "o", "u"]  # Initialise a new list containing the characters to search for
word = "No tracked branch configured for branch master or the branch doesn't exist. To make your branch track a remote branch " \
       "call, for example, git branch --set-upstream-to=origin/master master (show balloon) a"
# word = input("Please enter a word to search for")
# for letter in word:
#     if letter in vowels:
#         if letter not in dictionary_found_items:
#             dictionary_found_items[letter] = 1
#         else:
#             dictionary_found_items[letter] += 1

# Another way to write the statement above (because this is a very common occurrence in Python) is as follows, which reduces
# the lines to only one instead of two

for letter in word:
    if letter in vowels:
        dictionary_found_items.setdefault(letter, 0)  # Add KEY if not present and default value to zero
        dictionary_found_items[letter] += 1

print("--------------------RESULTS------------------------")
for key, value in sorted(dictionary_found_items.items(), reverse=False):
    if value != 0:
        print(key, "was found", value, "times")
