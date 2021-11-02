
#Task2
print("Hi")
your_name = input("Enter your name : ")
print("Let's start a game  " + your_name )
import random
Fav_Num = random.randint(1,100)
print("choose favourite number between 1 and 100")
fav = int(input("Enter your number :  "))
if fav <= 25:
    joke1 = print("Wow!You are lucky today")
    print(joke1)
elif int(fav>25 and fav<=50):
    joke2 = print("You are just amazing !")
    print(joke2)
elif int(fav>50 and fav<=90):
     joke3 = print("You are just few steps away from a treasure")
     print(joke3)
elif int(fav>90 and fav<=100):
        joke4 = "Congrats !  You are the winner of the day"
        print(your_name + "   " + joke4)
elif int(fav>100):
    joke5 = print("check your number")
    print(joke5)