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

# ##### Immutability ########
# """
# strings are immutable
# """

# change the name Sam to Pam
name = "Sam"

last_letters = name[1:]

print('P' + last_letters)