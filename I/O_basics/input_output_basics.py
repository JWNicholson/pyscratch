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


with open('/mnt/h/1.PersonalProjs/pyscratch/sometext.txt') as g_file:
    contents = g_file.read()
    print(contents)

with open('test.txt') as horseFace:
    horse = horseFace.read()
    print(horse)

