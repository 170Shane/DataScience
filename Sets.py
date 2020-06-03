# Sets are another Python Data Structure
# No duplicate values can exist is a set
# Sets are similar to lists and are created using a comma separated list of values, contained within curly braces
my_new_set = {"This", "is", "my", "new", "set", "This", "is", "my", "new", "set"}
# Data is stored UNORDERED
# Even if duplicate values are stored within the set, only distinct values are returned
print(my_new_set)

# Sets appear to be similar to dictionaries in that curly brackets are used, the difference being that dictionaries use a colon
# to separate the Key/Value pairs

# Sets can be created as follows:
vowels = {"a", "e", "i", "o", "u", "a", "e", "i", "o", "u"}
print("vowels = ", vowels)

# ......or like this, by passing an iterable sequence such as a string to the set function
vowels_alternate = set("aeiouaeiou")
print("vowels alternate", vowels_alternate)
vowels_alternate2 = set('123456789')
print("vowels alternate2", vowels_alternate2)

print("-----------------Exercise------------------")
vowels = {"a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "B", "z"}
word = "No tracked branch configured for branch master or the branch doesn't exist. To make your branch track a remote branch " \
       "call, for example, git branch --set-upstream-to=origin/master master (show balloon) a"

# Transform string to a set
set_from_string = set(word)
print(set_from_string)
print("-----------------Using UNION with SET------------------")
unioning = set.union(vowels, word)
print("Unioning two sets", unioning)
unioning = sorted(list(set.union(vowels, set_from_string)),
                  reverse=False)  # Sort by transposing to a List, which we can then sort
print("Unioning two sets", unioning)

print("-----------------Using DIFFERENCE with SET------------------")
difference = vowels.difference(set_from_string)
print("Difference between two sets is", difference)

print("-----------------Using SORTED with SET------------------")
print("Sorted set is", sorted(set(word)))  # Sorting a set returns a list

print("-----------------Using INTERSECTION with SET------------------")
difference = vowels.intersection(set_from_string)
print("Intersection of two sets is", difference)
