import random
playing=True
number=str(random.randint(0,9))
print("I will be giving you a number between 0 and 9, and you have to guess it")
print("the game will end when you get 1 hero")

while playing:
    guess=input("give your best guess! \n")
    if number == guess:
        print("you win the game!")
        print("the random number was", number)
        break
    else:
        print("your guess is wrong, please try again \n")
