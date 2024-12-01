import random
import time
print("NUMBER GUESSING GAME 5.0")

print()

while True:
    minimum = input("Minimum Number: ")
    while True:
        try:
            minimum = int(minimum)
            break
        except ValueError:
            print("It has to be a number, dumbass.")
            minimum = input("Minimum Number: ")
    maximum = input("Maximum Number: ")
    while True:
        try:
            maximum = int(maximum)
            break
        except ValueError:
            print("It has to be a whole number, dumbass.")
            maximum = input("Maximum Number: ")

    if minimum > maximum:
        print("The minimum number has to be smaller than the maximum number. Read a dictionary, dumbass.")
    else:
        print()
        c = random.randint(minimum, maximum)
        guess = int(input("Guess a random number between " + str(minimum) + " and " + str(maximum) + ": "))
        while True:
            if guess > maximum:
                print("It cant be higher than the MAXIMUM. read a dictionary, dumbass.")
                print()
                guess = int(input("Guess a random number between " + str(minimum) + " and " + str(maximum) + ": "))

            elif guess < minimum:
                print("It cant be lower than the MINIMUM. read a dictionary, dumbass.")
                print()
                guess = int(input("Guess a random number between " + str(minimum) + " and " + str(maximum) + ": "))

            elif guess < c:
                print("Too low. Dumbass.")
                print()
                guess = int(input("Guess a random number between " + str(minimum) + " and " + str(maximum) + ": "))

            elif guess > c:
                print("Too high. Dumbass.")
                print()
                guess = int(input("Guess a random number between " + str(minimum) + " and " + str(maximum) + ": "))

            else:
                print("Oh, wow. You got it. Still a dumbass, though, this is a luck game...")
                time.sleep(3)
                print()
                break