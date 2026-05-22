number=int(input("enter your guess number:"))
secret_number = 11
while number != secret_number:
    if number < secret_number:
       print("you're not close to the secret number and your number is too less, please try again")
    else:
       print("you're not close to the secret number and your number is too high, please try again")
number=int(input("enter your second guess number"))
while number != secret_number:
   if number < secret_number:
         print("you're not close to the secret number and your number is too less, please try again")
   else:
         print("you're not close to the secret number and your number is too high, please try again")
number=int(input("enter your third guess number:"))
while number !=secret_number:
    if number < secret_number:
        print("you're not close to the secret number and your number is too less, please try again")
    else:
        print("you're not close to the secret number and your number is too high, please try again")
number=int(input("enter your fourth guess number:"))
while number != secret_number:
    if number < secret_number:
        print("you're not close to the secret number and your number is too less, please try again")
    else:
        print("you're not close to the secret number and your number is too high, please try again")
        print("you have only one life left, try to guess the secret number correctly")
number=int(input("enter your fifth guess number:"))
while number == secret_number:
    print("Congratulations! You guessed the secret number!")