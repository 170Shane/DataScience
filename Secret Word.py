secret_word = "word secret" # set the secret word or phrase
user_response = ""
guess_counter = 0
guess_limit = 3

while user_response != secret_word and guess_counter <= guess_limit:
    user_response = input("Please guess the secret word : ")
    guess_counter = guess_counter + 1

if guess_counter > 1 and user_response == secret_word:
    print("Congratulations, you guessed the secret word in " + str(guess_counter) + " attempts")
elif guess_counter > 1 and user_response == secret_word:
    print("Congratulations, you guessed the secret word in " + str(guess_counter) + " attempt!")
else:
    print("You didn't guess the secret word and ran out of attempts!")



