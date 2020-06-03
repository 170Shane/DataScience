
# A regex is a special series of characters, also known as 'regular expressions', that defines a patter for complex
# string-matching functionality.

s = 'foo123bar'
# Simple string search - is the searched for string in the string itself
print('123' in s)  # True
print('1234' in s)  # False
print(s.find('123'))  # returns the index at which the string is found, -1 if not found
print(s.index('123'))  # returns the index at which the string is found, -1 if not found


#  .....or same thing within a function
def str_search(str_to_search, search_str):
    if search_str in str_to_search:
        return True
    else:
        return False


print(str_search('This is the string to search', 'is'))

#  Instead of searching for a hard-coded string such as '123', what about if we wanted to search for something more flexible,
#  such as whether or not the string contains ANY three number sequence

import re  # regex functionality within Python exists in a module named re

#  re.search(<regex>, <string>, <optional flags>) - Scans a string for a regex match
#  re.search returns a match object, or 'None' if no match is found
#  a match object is 'truthy'
print('Using re.search with static values ', re.search('123', s))  # returns <re.Match object; span=(3, 6), match='123'> where
# span=(3, 6) is the start and end index values for the search. This is similar to the slice notation [3:6]. 'match='123'
# indicates which characters from <string> matched.

if re.search('1234', s):
    print('Found a match')
else:
    print('No match')


#  In a regex, a set of characters specified in square brackets [] makes up a CHARACTER CLASS.
print('Using proper regex expressions searching for three consecutive numbers', re.search('[0-9][0-9][0-9]', s))

# [0-9] matches any single decimal digit character - any character between 0 and 9 inclusive.

#  The dot(.) character matches any character apart from a newline. Note that this character is not entered in
#  square brackets
print('Using proper regex expressions searching for the wildcard dot character', re.search('[f].', s))

# METACHARACTERS that match a single character
# Characters contained in square brackets represent a character class - an enumerated set of characters to match from.
print('Using proper regex expressions searching for character classes', re.search('ba[a-r]', s))

#  A metacharacter sequence of [artz] matches any single 'a', 'r', 't', or 'z' character
#  A character class range matches any single character in the range
print('Using proper regex expressions searching for character class range a-r', re.search('[a-r]', s))
