import random

x = input("pick a number 1-100:  ")
y = random.randint(1,100)
print("you picked " + x + " and the number was " + str(y))

if int(x) > y:
    print("Too High!")

if int(x) < y:
    print("Too Low!")

if int(x) == y:
    print("Thats Correct!")
