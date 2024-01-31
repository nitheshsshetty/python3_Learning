import random

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissor"]

def watson():
    choice = random.choice(options)
    return choice
    
while True:
    user_input = input("\nType Rock/paper/scissor or q to quit ===>  ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print(" \n Thats not a valid input")
        continue
    computer_choice = watson()
    #elif:user_input == choice:
    
    print(f"\nUser choice ===> {user_input} \ncomputer choice ===> {computer_choice}")
    
    if user_input == "rock" and computer_choice == "scissor":
        user_wins += 1
        continue
    elif user_input == "paper" and computer_choice == "rock":
        user_wins += 1
        continue
    elif user_input == "scissor" and computer_choice == "paper":
        user_wins += 1
        continue
    elif user_input == computer_choice :
        print("\nDraw with no points to either ")
        continue
    else:
        print("\nYou Lost !")
        computer_wins += 1

print(f"\n Number of times User wins is {user_wins} \n Number of times computer wins is {computer_wins}")
print("\n Good bye !!")

