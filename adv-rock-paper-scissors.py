import random
import math


def is_strong(user_input, computed_desicion):
    i = options.index(user_input)
    if (i+x)%n+1 < (i+1)%n:
        stronger_ones = options[(i+1)%n:] + options[:(i+x+1)%n]
    else:
        stronger_ones = options[(i+1)%n:(i+x)%n+1]
    # print(stronger_ones)
    if computed_desicion in stronger_ones:
        return False
    return True

usernames_with_ratings = []
with open("rating.txt") as file:
    for f in file.readlines():
        usernames_with_ratings.append(f.replace("\n", ""))
usernames_with_ratings = {ur.split()[0]: int(ur.split()[1]) for ur in usernames_with_ratings}

name = input("Enter your name:")
print(f"Hello, {name}")
score = usernames_with_ratings.get(name, 0)
options = input()
if options == "":
    options = ['rock', 'paper', 'scissors']
else:
    options = options.split(",")
n = len(options)
x = math.floor(n/2)
print("Okay, let's start")

while True:
    computed_desicion = random.choice(options)
    user_input = input()
    if user_input == '!rating':
        print(score)
    elif user_input == "!exit":
        break
    elif user_input in options:
        if user_input == computed_desicion:
            print(f"There is a draw ({computed_desicion})")
            score += 50
        elif is_strong(user_input, computed_desicion):
            print(f"Well done. The computer chose {computed_desicion} and failed")
            score += 100
        else:
            print(f"Sorry, but the computer chose {computed_desicion}")
    else:
        print("Invalid input")
print("Bye!")