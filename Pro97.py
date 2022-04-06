import random

number = random.randrange(0, 10)
chances = 0

while chances < 5:
    guess = input("Guess the number: ")
    if guess == number:
        print("Congradulations, YOU WON!!!")
        break
    else:
        print("Wrong answer")
    chances += 1
    if not chances < 5:
        print("YOU LOSE!!! The number is", number)
