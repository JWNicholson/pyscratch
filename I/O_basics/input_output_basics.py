 #f = open('test.txt', 'r')
#g = open('/mnt/h/1.PersonalProjs/pyscratch/sometext.txt')


# print(f.read())

# print("++++++++++++++++++++++++")
# # in order to read the file again, set the cursor back to zero
# # otherwise you get a blank return
# f.seek(0)

# print(f.read())

# print('**************')

# # return as a list
# f.seek(0)
# print(f.readlines())
# f.close()

# print(g.read())

"""
    New and better way - combines read and close functions
"""


# with open('/mnt/h/1.PersonalProjs/pyscratch/sometext.txt') as g_file:
#     contents = g_file.read()
#     print(contents)

# with open('test.txt') as horseFace:
#     horse = horseFace.read()
#     print(horse)
"""
r = read
w = write only (overwrites files or creates new one if it doesn't exist)
a = append
r+ = read and write
w+ = writing and reading (Overwrites existing file or creates a new file if it doesn't exist)
"""
# write in to file
with open('readwrite.txt', mode='r') as f:
    print(f.read())


#append
with open('readwrite.txt', mode='a') as f:
    f.write('\nLater Gator')

with open('readwrite.txt', mode='r') as f:
    print(f.read())

# create cause it dont exists yet
with open('giggedy.txt', mode='w') as f:
    f.write('Quagmire')

with open('giggedy.txt',mode='r') as f:
    print(f.read())