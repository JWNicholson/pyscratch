"""
    Dictionaries are 
    -{key:value} pairs
    -unordered
    -can't be sorted
"""
my_dict = {'key1':'value1','key2':'value2'}

## get the value in key1
# x = my_dict['key1']
# print(x)

######
# price_lookup = {'apple':'0.99', 'oranges':'1.50','pears':'2.50'}

# ## get price of apple
# x = price_lookup['apple']
# print(x)

##
# y = {'a1':['1,2,3'], 'a2':['4,5,6'], 'a3':{'insideKey': 10}}
# x = y['a2']
# print(x)
# print(y['a3']['insideKey'])

# a_list = {'key1':['a','b','c']}
# b = a_list
# ## get the letter c
# c = b['key1'][2]
# print(a_list)
# print(c)
# ## captilize the result
# print(c.upper())

## add element
d = {'k1': 10,'key2': 20 }
d['k3'] = 30
print(d)

## change a value
d['k1'] = 'New Value'
print(d)

## see all the keys
print(d.keys())

## see all the values
print(d.values())

## see paired items (result is a tuple)
print(d.items())