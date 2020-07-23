f = open('test.txt', 'r')



print(f.read())

print("++++++++++++++++++++++++")
# in order to read the file again, set the cursor back to zero
# otherwise you get a blank return
f.seek(0)

print(f.read())

print('**************')

# return as a list
f.seek(0)
print(f.readlines())



