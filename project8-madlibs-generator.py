import string

with open("project8-story.txt","r")as f:
    story=f.read() 
    print(story)
target_start = "<"
target_end = ">"
start_of_word = -1
words = set()
for i ,char in enumerate(story):
    if char == target_start :
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = story[start_of_word:i+1]
        words.add(word)
        start_of_word = -1
print(words)

answers = {}
for word in words:
    answer = input(f"Enter word for {word} : ")
    answers[word]=answer
print(answers)

for word in words:
    story=story.replace(word,answers[word])
    
print(story)