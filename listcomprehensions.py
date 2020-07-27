"""
first example not the most efficient
"""
mystring = 'hello'
#mylist = []

# for letter in mystring:
#     mylist.append(letter)



######Better (list comprehension)######
# mylist = [letter for letter in mystring]

# print(mylist)

# alist = [x for x in 'buffalo']
# print(alist)

# whatlist = [num for num in range(0,11)]
# print(whatlist)

# squarelist = [num**2 for num in range(0,11)]
# print(squarelist)


# ifsquarelist = [x for x in range(0,11) if x%2 == 0]
# print(ifsquarelist)

# ifsquareofevenlist = [x**2 for x in range(0,11) if x%2 == 0]


celcius = [0, 20, 30, 40]
fahrenheit = [( (9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

results = [x if x%2==0 else "Odd" for x in range(0,11)]
print(results)