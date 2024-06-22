
print("welcome to my comouter quiz!")

player = input("Do you wanna play?")

if player != "yes":
    quit()

print("Okay! Let's play!")
score = 0 

answer = input("What does ASEAN stands for? ")

if answer == "Association of Southeast Asia Nations":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many countires are there in ASEAN? ")

if answer == "10":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Is Indoenesia part of ASEAN? ")

if answer == "No":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
print("You got " + str((score / 3) * 100) + "%.")



