# Exercise 14:
#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.


names = ["Michele", "Robin", "Sara", "Michele"]
def dropdup(names):
    s = set(names)
    ans = list(s)
    print(names)
    print(ans)
dropdup(names)
    