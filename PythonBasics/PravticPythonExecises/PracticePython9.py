# Exercise 9:
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
g = random.randint(1,10)
c = 0
while True:
    i = input("Enter a number:")
    if i == "exit":
        print(c)
        break
    c = c+1
    if(g<int(i)):
        print("too high")
    elif(g>int(i)):
        print("too low")
    else:
        print("exactly right")
    
