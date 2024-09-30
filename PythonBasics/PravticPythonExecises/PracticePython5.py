## Exercise 5:
# Take two lists, say for example these two: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]and write a program that returns a list that contains only the elements that are common between the lists (without duplicates)..Extras:Randomly generate two lists to test this.Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
#1
import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
d = []
for x in a:
    if(x in b):
        c.append(x)
print(set(c))
#2
random_list1 = [random.randint(1, 100) for _ in range(10)]
random_list2 = [random.randint(1,100) for _ in range(10)]
print(random_list1)
print(random_list2)
for x in random_list1:
    if(x in random_list2):
        d.append(x)
print(set(d))
#3
print(set([x for x in a if x in b]))
print(set([hh for hh in random_list1 if hh in random_list2]))
