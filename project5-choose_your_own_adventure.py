name = input("Type your name ")
print(f"Welcome {name} welcome to thsi adventure ")
answer = input("You are on a dirt road which has come to an end- which way do you want to go LEFT or RIGHT ? ===> ").lower()
if answer == "left":
    answer = input("Now you have come near water ! Do you want to swim through ? Yes or No  ===>  ").lower()
    if answer == "yes":
        print("AH OOHH ...you are eaten by alligator you lost !!")
    else:
        print("you are safe and you won !!")

elif answer == "right":
    answer = input("Now you have come near mountain ! Do you want to clim through ? Yes or No  ===>  ").lower()
    if answer == "yes":
        print("AH OOHH ...you are dehydrated by walkin and you lost !!")
    else:
        print("you are safe and you won !!")

else: print("Not a valid input !!")

