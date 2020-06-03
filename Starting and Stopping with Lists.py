# STARTING AND STOPPING WITH LISTS
book = "The Hitchhiker's Guide to the Galaxy"
print("The book string value is " + book)

booklist = list(book)
print("Now the book is a list that contains  " + booklist.__str__())

# Starting at index position 0, all characters up to the end position 4
print(booklist[0:3])  # doesn't actually include position 3 (item 4)

# Join the characters from the list back into a string
print(''.join(booklist[0:3]))

# Join the last 6 characters and change to a string value
# Code retrieves all characters after the Start value (-6)
print(''.join(booklist[-6:]))

# STEPPING WITH LISTS
backwards = booklist[::-1]  # Default Start/Stop values and simply steps back in -1 intervals
print(backwards)  # Print the List values
print("The list back into a string value is """ + ''.join(backwards))  # Turn the List back into a string

# [START:STOP:STEP]
# Get every second value
every_other = booklist[::2]  # START AND STOP USE THE DEFAULT VALUES (START = 0, STOP = MAX_VALUE_FOR_LIST)
print("Every other value is " + every_other.__str__())
print("Every other value joined as a string is " + ''.join(every_other))

# 'SLICING'
#  It is possible to start and stop anywhere in a list - this is referred to as SLICING
#  Start at index 4 (position 5) and go up to but don't include index position 14 (position 15)
print("Getting characters from a list and changing them to a string " + ''.join(booklist[4:14]))

# Slice out the word Hitchhiker and display it in reverse order
print(''.join(booklist[13:3:-1]))

# Slicing doesn't just work with lists - it will work in Python with any sequence
# accessing it with [START:STOP:STEP]
print("Hello, I am working from home"[:10:1])
print("Hello, I am working from home"[:10:2])
print("Hello, I am working from home"[:10:3])
print("Hello, I am working from home"[:10:4])

