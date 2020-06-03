from math import *

character_name = "Paul"
character_age = 25
is_male = True

# comment

print("There once was a man named " + character_name
      + ", ")
print("he was " + str(character_age) + " years old.")

print("He really liked the name " + character_name + ", ")
print("but he didn't like being " + str(character_age))

#strings
print(character_name[2])
print(character_name.index("L".lower()))

#numbers
# print(max(5,7,8,9,8,987,10))
# print(floor(5.51651))
# print(ceil(5.1651))
# print(sqrt(6.9651))
# print(int(sqrt(5.1651)))

# user input
# response = input("Please enter something to help me")
# print("You entered " + response + "!")

# calculator
# int1 = input("Please enter your first number")
# int2 = input("Please enter your second number")
# result = float(int1) * float(int2)
# print("The answer is " + str(result) + "!")

# lists
friends = ["Harry", "Shane", "Shaun", "Julie"]
print(friends[0])
print(friends)
print(friends[1:3])
friends.remove("Harry")
print(friends)

# lists.extend adds another list to a list
# lists.append adds an item to the end of the list
# lists.insert adds an item to the list at the specified position
# lists.remove removes an item from the list - need to specify the the actual list value rather than the position
# lists.clear removes all elements from the list
# lists.pop - gets rid of the last element on a list
# lists.index("value") returns the index position if the value exists
# lists.count("value") returns the count of items equal to the parameter
# lists.sort sorts a list
# lists.reverse reverses a list
# lists.copy creates a copy of the list (friends2 = friends.copy())