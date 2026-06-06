import random
while True:
    user_action = input("enter a choice (rock, paper, scissors):")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"both player selected {user_action}. it's a tie!")
    elif (user_action == "rock" and computer_action == "scissors") or\
         (user_action == "paper" and computer_action == "rock") or\
         (user_action == "scissors" and computer_action == "paper"):
        print("you win!")
    else:
        print("you lose!")
    play_again=input("play again? (y/n):")
    if play_again != "y":
        break
