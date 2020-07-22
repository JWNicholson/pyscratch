""""
    Tuples are IMMUTABLE
"""

t = (1,2,3)
t2 = ('one',2)
mylist = [1,2,3]

# print(type(t))
# print(type(mylist))
# print(len(t))
# print(t[0])
# print(t[-1])

t3 = ('a','a','b')
# count how many times 'a' is in this tuple
x = t3.count('a')
print(x)

# what index does 'a' appear first
y = t3.index('a')
print(y)

