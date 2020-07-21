"""
    Lists ARE Mutable
"""
a_list = [1,2,3]
mixed_list = ['STRING', 50, 24, 89]
b_list = ['one', 'two', 'three']

# # check length
# print(len(a_list))

# # slicing 
# # index 1 to end
# print(b_list[1:])

# #concat
# x_list = a_list + mixed_list
# print(x_list)

# #change an element
# x_list[0] = 'ONE TEXT'
# print(x_list)

# #add element to end of list
# x_list.append('Six')
# print(x_list)

# # remove element from end of list
# y = x_list.pop()
# print(y)
# z = x_list
# print(z)

#sort & reverse

y_list = ['e','c','a','d','b']
num_list = [5,3,1,8,10]

#sort() sorts the list in place, so assigning the list to a variabl must occur AFTER the sort()
y_list.sort()
print(y_list)
new_y_list = y_list
print(new_y_list)

print("-------------------------------------")
print(num_list)

num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)