import random 
import time
MIN_VALUE = 3
MAX_VALUE = 15
OPERATOR = ["+","-","*"]
COUNT = 5

def generate_problem():
    Left = random.randint(MIN_VALUE,MAX_VALUE)
    right =  random.randint(MIN_VALUE,MAX_VALUE)

    operator = random.choice(OPERATOR)
    expr = str(Left) + " " + operator + " " +str(right)
    answer = eval(expr)
    
    return expr ,answer

input("Press enter to start the game ")
start = time.time()
print("=============================")
for i in range(COUNT):
    expr,answer = generate_problem()
    while True:
        ans = input(f"Problem #{i+1} : {expr} = ")
        if ans != str(answer):
            continue 
        else : 
            break

end =time.time()
total = str(round(end-start, 2))
print(f"You took {total} seconds" )
print("=============================")
print("Thanks for playing  .") 
