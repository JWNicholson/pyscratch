# Shell Game - guess wich shell the ball is under

"""
Use a list to represent shells and ball
Will not show the shuffle, making the guess completely random
"""
# example of shuffling a list
import random
from random import shuffle

# dlist = [1,2,3,4,5,6,7]
# result = shuffle(dlist)# this will not return anything
# #print(result)

# def shuffle_list(alist):
#     shuffle(alist)
#     return alist

# result = shuffle_list(dlist)
#print(result)

##################################
"""
g_list represents the 3 shells. O represents the ball
1. set Initial list
2. shuffle list
3. user guesses
4. check user's guess
"""


def shuffle_list(game_list):
    shuffle(game_list)
    return game_list

def player_guess():
    guess = ''
    # ask for player's guess and validate input
    while guess not in ['0','1','2']:
        guess = input("Pick a number - 0, 1, or 2")# input always returns a string
    return int(guess)


def check_guess(game_, guess):
    # check the value of player_guessed at guess index position
    if game_list[guess] == 'O':
        print("You win")
    else:
        print("Wrong")
        print(game_list)

## Logic ---

# inital list
game_list = [' ', 'O', ' ']

#shuffle list
mixedup_list = shuffle_list(game_list)

#user guess
guess = player_guess()

# check guess
check_guess(mixedup_list,guess)



