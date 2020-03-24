import random

print("-------------------------------------")
print("       GUESS THAT NUMBER GAME")
print("-------------------------------------")
print()

the_number = random.randint(0, 100)
guess = -1
name = input("Enter your name : ")

while the_number != guess:
    guess_text = input("Guess a number between 0 and 100 : ")
    guess = int(guess_text)
    if guess > the_number:
        print("Sorry, {0}, Your guess of {1} is too high.".format(name, guess))
    elif guess < the_number:
        print("Sorry, {0}, Your guess of {1} is too low.".format(name, guess))
    else:
        print("Excellent guess, {}. You Win! The number was {}".format(name, guess))

print("Done!")



