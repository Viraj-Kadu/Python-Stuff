#Exercise 6:
#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

s1 = input("Enter the string:")
s2 = ""
n = len(s1)
for c in range(1,n+1):
    s2 = s2 + s1[n - c]
print(s1==s2)
print(s1,s2)
