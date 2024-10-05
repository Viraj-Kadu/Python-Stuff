# Exercise 15:
#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

s = input("Enter your string:")
print(s)
listofs = s.split(" ")
listofs.reverse()
ans = " ".join(listofs)
print(ans)
