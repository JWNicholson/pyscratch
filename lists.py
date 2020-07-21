"""
    Lists ARE Mutable
"""
a_list = [1,2,3]
mixed_list = ['STRING', 50, 24, 89]
b_list = ['one', 'two', 'three']

# check length
print(len(a_list))

# slicing 
# index 1 to end
print(b_list[1:])

#concat
x = a_list + mixed_list
print(x)

