
#requirements
#IN THIS PROGRMA WE ASK USER SOME QUESTIONS IF CORRECT ANSWERS WE GIVE 1 POINT 
#AT THE END OF THE GAME WE TALLY THE NUMBERS OF POINTS EARNED AT THE END 

print("Welocme to my computer quiz")
playing = input("Do you want to play game Y/N ")
print(playing)

if playing != 'yes':
    quit()

print("Lets play the game..")
count = 0 

answer = input ("What does CPU standand for ? ")
if answer.lower() == "central processing unit":
    print("correct answer !")
    count = count+1
    #print(f"You scored {count} points  !!!!!")
else : 
    print("oops wrong answer")

answer = input ("What does GPU standand for ? ")
if answer.lower() == "graphics processing unit":
    print("correct answer !")
    count = count+1
    #print(f"You scored {count} points  !!!!!")
else : 
    print("oops wrong answer")


answer = input ("What does RAM standand for ? ")
if answer.lower() == "random acess memory":
    print("correct answer !")
    count = count+1

    #print(f"You scored {count} points  !!!!!")
else : 
    print("oops wrong answer")

answer = input ("What does PSU standand for ? ")
if answer.lower() == "power supply unit":
    count = count+1
    print("correct answer !")
    
else : 
    print("oops wrong answer")

print(f"You got {count} questions correct  !!!!!")
print(f"You scored {count/4 * 100 }%  ")

print("Thanks for playing")
