# Task1
import random
myname = input("Enter your Name: ")
mynumber = random.randint(1, 10)

print("Hello  " + myname)
guess = int(input("Enter a number between 1 and 10 : "))
if guess == mynumber:
    print("Wow!" +"  " + myname + "You guessed my lucky number")
else:
    print("Try again")
