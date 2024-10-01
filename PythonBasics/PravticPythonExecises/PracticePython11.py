# Exercise 12:
#Ask the user for a number and determine whether the number is prime or not. Take this opportunity to practice using functions, described below.
i = int(input("Enter the number:"))
for x in range (2,i):
    if(i%x==0):
        print("Not Prime")
        break
print("Prime")