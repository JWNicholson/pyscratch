## strings - Indexing & Slicing#############

# s = 'Whatnowhomer?'

# # print 5th element
# print(s[4])

# #print last element when unkonwn length
# print(s[-1])

# ## Slicing ##

# #start at index 2, go to the end
# print(s[2:])

# #start at beginning and go to 4th index
# print(s[:4])

# # get a subsection - indexes 3,4,5 (but not 6) 
# print(s[3:6])

# # get a subsection
# print(s[1:3])

# #get everything in a stepsize of 1
# print(s[::])

# #get everything in a stepsize of 2
# print(s[::2])

# #get everything in a stepsize of 3
# print(s[::3])

# #get everything starting at 2, up to index 12 in a stepsize of 3
# print(s[2:12:3])

# # reverse the string
# print(s[::-1])

# ##### String Properties and Methods ########
# """
# strings are immutable
# """

# Concatenate - change the name Sam to Pam
# name = "Sam"

# last_letters = name[1:]

# print('P' + last_letters)

# # Multiplication of letters
# a = 'words '
# a_1 = a * 4
# print(a_1)

## show methods avaialble for data type (in this case a string)
### assign a variable
### type the variable plus dot for popup with available methods 
#x = 'the string thing'
# #x.
# x = x.upper()
# print(x)

# split-default splits on spaces - makes a list
# print(x.split())

# #split - on the t's - includes the spaces
# print(x.split('t'))

#### String Formatting
"""
.fromat() method
"""
# print('The String {}'.format('Thing'))

# ## insert by index
# print('Eat {0} {2} {1}'.format('more','sandwiches', 'possum'))
# print('Eat {a} {b} {b}'.format(a='more', b='sandwiches', c='possum'))

## Newer Better Method
# name = "Albert"
# print(f"{name} is one of the three Kings of the Blues")

## Float fotmatting {value:width.precision.f} width includes white space in front
# result = 100/888
# print("The result is {r:1.3f}".format(r=result))



