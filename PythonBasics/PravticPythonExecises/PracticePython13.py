# Exercise 13:
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
def fibo(j):
    c1 = 1
    c2 = 1
    while j-2:
        temp = c2
        c2 = c1 + c2
        c1 = temp
        j -= 1
    print(c2)
i = int(input("Enter a number:"))
if i<=0: print("Enter valid number")
elif i<=2 : print(1)
else : fibo(i)

        


