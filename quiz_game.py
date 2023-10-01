""" Quiz game inspired by Tech With Tim's first project in the 5 Mini Python Projects video """

playing = input("A definiton of a word will be given and you must guess the word, got it? (yes/no)")

if playing.lower() != "yes":
    quit()

print("Alright let's play :) ")
score = 0

answer = input("To grasp mentally: ")
if answer.lower() == "comprehend":
    print("Good Job")
    score += 1
else:
    print("Wrong it's: Comprehend")

answer = input("To tolerate delay: ")
if answer.lower() == "patience":
    print("Good Job")
    score += 1
else:
    print("Wrong it's: Patience")

answer = input("Observation of facts or events: ")
if answer.lower() == "experience":
    print("Good Job")
    score += 1
else:
    print("Wrong it's: Experience")

answer = input("The outside of something: ")
if answer.lower() == "exterior":
    print("Good Job")
    score += 1
else:
    print("Wrong it's: Exterior")

answer = input("In a way that relates to Tech: ")
if answer.lower() == "technologically":
    print("Good Job")
    score += 1
else:
    print("Wrong it's: Technologically")

print(f"You got {score}/5")
