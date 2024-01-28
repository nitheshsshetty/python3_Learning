#Number guessing game 
#SIMPLE GAME WITH USER GETTING CHANCE TO GUESS THE NUMBER CORRECT GENRATED GRANDOMLY BY THE PROGRAM AND SCORE ACCORDINGLY 

import random
TOP_RANGE = 6
count = 1 

top_of_range = input("Type a number : ")
if top_of_range.isdigit():
    top=int(top_of_range)
    if top <= 0:
        print("Please type a number larger than zero next time ")
        quit()
else:
     print("Please type a number next time")
     quit()

random_number=random.randint(0,TOP_RANGE)

while True:
    guess = int(input("Make a guess"))
    if guess == random_number:
        print("You have guessed the correct number ")
        break
    elif guess > random_number:
        
        print("Your guess was above the number !")
    else:
        print("Your guess was below the number !")
    count += 1
    continue

print(f"\n \n  you got it in {count} guesses")

