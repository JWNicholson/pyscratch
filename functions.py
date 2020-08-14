
# def check_even_list(num_list):
#     for number in num_list:
#         if number % 2 == 0:
#             return True
#         else:
#             pass#don't do anything


# print(check_even_list([3,5,7,9]))

# print(check_even_list([2,4,6,7]))

# print(check_even_list([1,3,2]))# returns True if there is at least one even in the list (as soon as it finds the first one)


# #Better - loop wont quit if it finds returns True
# def check_even_list(num_list):
#     for number in num_list:
#         if number % 2 == 0:
#             return True
#         else:
#             pass

#     return False


#Go through the entire loop and add evens to the list before return the list (results)
def check_even_list(num_list):
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)

        else:
            pass

    return even_numbers