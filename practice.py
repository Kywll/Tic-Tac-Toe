
#boxes to fill, X and O, win condition/patterns

#Player Input Choices
#make a library array

#Store Players Inputs
#translate player input to board then print it

#Make A List of possible Win Conditions

#Compare the Player's Choices to win conditions

#Determine Who Wins

import random

board_example = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

print("Enter the Number of the Board you want to place on")

print(board_example[0])
print(board_example[1])
print(board_example[2])

print("")

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

game_over = False
x_input = None
o_input = None

available_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player_side = None
versus_bot = False

def match_input(num, xo):
    if xo == 1:
        if num == 1:
            board[0][0] = 'X'
            available_choices.remove(1)
        elif num == 2:
            board[0][1] = 'X'
            available_choices.remove(2)
        elif num == 3:
            board[0][2] = 'X'
            available_choices.remove(3)
        elif num == 4:
            board[1][0] = 'X'
            available_choices.remove(4)
        elif num == 5:
            board[1][1] = 'X'
            available_choices.remove(5)
        elif num == 6:
            board[1][2] = 'X'
            available_choices.remove(6)
        elif num == 7:
            board[2][0] = 'X'
            available_choices.remove(7)
        elif num == 8:
            board[2][1] = 'X'
            available_choices.remove(8)
        elif num == 9:
            board[2][2] = 'X'
            available_choices.remove(9)
        else:
            pass
    elif xo == 0:
        if num == 1:
            board[0][0] = 'O'
            available_choices.remove(1)
        elif num == 2:
            board[0][1] = 'O'
            available_choices.remove(2)
        elif num == 3:
            board[0][2] = 'O'
            available_choices.remove(3)
        elif num == 4:
            board[1][0] = 'O'
            available_choices.remove(4)
        elif num == 5:
            board[1][1] = 'O'
            available_choices.remove(5)
        elif num == 6:
            board[1][2] = 'O'
            available_choices.remove(6)
        elif num == 7:
            board[2][0] = 'O'
            available_choices.remove(7)
        elif num == 8:
            board[2][1] = 'O'
            available_choices.remove(8)
        elif num == 9:
            board[2][2] = 'O'
            available_choices.remove(9)
        else:
            pass



#Bot Algo
#Choose wether Bot is X or O
#Make Bot Choose between 1-9
#Make sure bot dont choose occupied spaces in board
#Translate Bot Choices
#Output if Bot Won

def bot():
    player_side = None

    
    
    bot_enabled = False
    bot_side = None
    bot_choice = random.choice(available_choices)


    choice_one = None
    choice_two = None
    choice_three = None
    choice_four = None
    choice_five = None
    choice_six = None
    choice_seven = None
    choice_eight = None
    choice_nine = None

    
    
    



#Used to compare if a row of list has all X or O
X = ['X', 'X', 'X']
O = ['O', 'O', 'O']

#'''
def win_conditioner():
    global game_over
    win_con_one = [board[0][0], board[0][1], board[0][2]]
    win_con_two = [board[1][0], board[1][1], board[1][2]]
    win_con_three = [board[2][0], board[2][1], board[2][2]]
    win_con_four = [board[0][0], board[1][0], board[2][0]]
    win_con_five = [board[0][1], board[1][1], board[2][1]]
    win_con_six = [board[0][2], board[1][2], board[2][2]]
    win_con_seven = [board[0][0], board[1][1], board[2][2]]
    win_con_eight = [board[0][2], board[1][1], board[2][0]]

    x1 = any(i != j for i, j in zip(X, win_con_one))
    x2 = any(i != j for i, j in zip(X, win_con_two))
    x3 = any(i != j for i, j in zip(X, win_con_three))
    x4 = any(i != j for i, j in zip(X, win_con_four))
    x5 = any(i != j for i, j in zip(X, win_con_five))
    x6 = any(i != j for i, j in zip(X, win_con_six))
    x7 = any(i != j for i, j in zip(X, win_con_seven))
    x8 = any(i != j for i, j in zip(X, win_con_eight))

    o1 = any(i != j for i, j in zip(O, win_con_one))
    o2 = any(i != j for i, j in zip(O, win_con_two))
    o3 = any(i != j for i, j in zip(O, win_con_three))
    o4 = any(i != j for i, j in zip(O, win_con_four))
    o5 = any(i != j for i, j in zip(O, win_con_five))
    o6 = any(i != j for i, j in zip(O, win_con_six))
    o7 = any(i != j for i, j in zip(O, win_con_seven))
    o8 = any(i != j for i, j in zip(O, win_con_eight))

    if x1 == False or x2 == False or x3 == False or x4 == False or x5 == False or x6 == False or x7 == False or x8 == False:
        print("X WON")
        game_over = True
    elif o1 == False or o2 == False or o3 == False or o4 == False or o5 == False or o6 == False or o7 == False or o8 == False:
        print("O WON")
        game_over = True
#'''
        
while game_over == False:
    if versus_bot == False:
        x_input = int(input("Player X Input: "))
        while x_input not in available_choices:
             x_input = int(input("Option already taken, try another: "))
        o_input = int(input("Player O Input: "))
        while o_input not in available_choices:
             o_input = int(input("Option already taken, try another: "))
    

    match_input(x_input, 1)
    match_input(o_input, 0)

    print("")

    print("Current Board")
    print(board[0])
    print(board[1])
    print(board[2])

    print("")

    win_conditioner()


'''
win_conditioner()


print(win_con_one)


#Gives False if the lists getting compared is equal(NO IDEA HOW THIS WORKS but it works)
c = any(i != j for i, j in zip(board[0], X))
print(c)

if c == False:
    #print("YOU WON")

    
#Gives elements that are present in two lists comapared(Not what I want, I need to get booleans)
combine = set(board[0]).intersection(X)
print(combine)

'''



