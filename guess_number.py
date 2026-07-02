import random

# Here's your first challenge!
# Make a game that generates a random number from 0 - 10
# Make the user guess the number, and give a response depending on whether they are right or wrong

# Challenge 1: Make the program say higher or lower based on the guess accurately
# Challenge 2: Limit the number of guesses that the player gets

# number = random.randint(1,10)

number = random.randint(1, 10)
print("I'm thinking of a number between 0 and 10. What it is?")

number_of_guesses = 3

while True:
    user_number = input("Enter number: ")
    try:
        user_number = int(user_number)
    except ValueError:
        print("You're just trying to break my code, aren't you?")
        continue
    if int(user_number) > 10: 
        print("I said 0 - 10, am I muted?")
        continue
    if int(user_number) < 0: 
        print("Thats...not fair.")
        continue
    elif int(user_number) > number:
        print("Where is your head, in the clouds? You're too high!")
    elif int(user_number) < number:
        print("You're as short as me! guess higher...")
    elif int(user_number) == number:
        print("10 years later...You got it!")
        break
    print("Guess again!")
    if user_number != number:
        print(f'You have {number_of_guesses} tries left.')
        number_of_guesses -= 1
    if number_of_guesses == -1:
        print(f"You're taking too long! The number was: {number}")
        break