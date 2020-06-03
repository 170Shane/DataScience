from random import *  # import the random module, so that we have access to the randint function

secret_number = randint(1, 20)  # generate a random number between 1 and 50


print('I am thinking of a number between 1 and 50')

# Ask the player to guess six times
for guessesTaken in range(1, 7):
    # guess = int(input(print('Take a guess : ')))
    guess = int(input())
    if guess < secret_number:
        print('Too low')
    elif guess > secret_number:
        print('Too high')
    else:
        break # this is the correct number


if guess == secret_number:
    print('You guessed it in', guessesTaken, 'guesses')
else:
    print('Sorry, you failed')