# Title of the application
print("Welcome to Quiz Game!")
name = input("Enter Your Name: ")
while name == "" :
    name = input("Enter Your Name: ")
agree = input(f"Hello {name}, do you want to play the game: ").lower()

if agree == "yes":
    print("Let's play the game!")

else:
    print("Thank you. bye!")
    quit()

score=0
# Question 1

q1 = input("Question 1: Are you human? ").lower()

if q1 == "yes":
    score = score+1
    print(f"Correct answer! Your score is {score}")

else:
    print("Wrong answer!")

q2 = input("Question 2: What is the most beautiful country in the world? ").lower()

if q2 == "india":
    score = score + 1
    print(f"Correct answer! Your score is {score}")

else:
    print("Wrong answer!")

score_percentage = (score/2)*100
print(f"You have got {score_percentage}%")

