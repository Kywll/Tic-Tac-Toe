
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

player_side = 'X'
bot_side = None
if player_side == 'X':
    bot_side = 'O'
else:
    bot_side = 'X'

versus_bot = True
bot_choice = random.choice(available_choices)



def print_board(first, second):
    #Prints Current Board
    if first == 1:
        print("")
    
    print("Current Board")
    print(board[0])
    print(board[1])
    print(board[2])

    if second == 1:
        print("")
    
def match_input(num, xo):
    
    if num == 1:
        if xo == 'X':
            board[0][0] = 'X'
        elif xo == 'O':
            board[0][0] = 'O' 
        available_choices.remove(1)
    if num == 2:
        if xo == 'X':
            board[0][1] = 'X'
        elif xo == 'O':
            board[0][1] = 'O'
        available_choices.remove(2)
    if num == 3:
        if xo == 'X':
            board[0][2] = 'X'
        elif xo == 'O':
            board[0][2] = 'O'
        available_choices.remove(3)
    if num == 4:
        if xo == 'X':
            board[1][0] = 'X'
        elif xo == 'O':
            board[1][0] = 'O'
        available_choices.remove(4)
    if num == 5:
        if xo == 'X':
            board[1][1] = 'X'
        elif xo == 'O':
            board[1][1] = 'O'
        available_choices.remove(5)
    if num == 6:
        if xo == 'X':
            board[1][2] = 'X'
        elif xo == 'O':
            board[1][2] = 'O'
        available_choices.remove(6)
    if num == 7:
        if xo == 'X':
            board[2][0] = 'X'
        elif xo == 'O':
            board[2][0] = 'O'
        available_choices.remove(7)
    if num == 8:
        if xo == 'X':
            board[2][1] = 'X'
        elif xo == 'O':
            board[2][1] = 'O'
        available_choices.remove(8)
    if num == 9:
        if xo == 'X':
            board[2][2] = 'X'
        elif xo == 'O':
            board[2][2] = 'O'
        available_choices.remove(9)


#Used to compare if a row of list has all X or O
X = ['X', 'X', 'X']
O = ['O', 'O', 'O']

def win_conditioner():
    out_of_moves = {}
    global game_over
    win_con_one = [board[0][0], board[0][1], board[0][2]]
    win_con_two = [board[1][0], board[1][1], board[1][2]]
    win_con_three = [board[2][0], board[2][1], board[2][2]]
    win_con_four = [board[0][0], board[1][0], board[2][0]]
    win_con_five = [board[0][1], board[1][1], board[2][1]]
    win_con_six = [board[0][2], board[1][2], board[2][2]]
    win_con_seven = [board[0][0], board[1][1], board[2][2]]
    win_con_eight = [board[0][2], board[1][1], board[2][0]]

    #Gives out False value if a winning pattern has all X which would X won
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
    
    if available_choices == out_of_moves:
        game_over = True
        print("DRAW")

#Bot Algo
#Choose wether Bot is X or O
#Make Bot Choose between 1-9
#Make sure bot dont choose occupied spaces in board
#Translate Bot Choices
#Output if Bot Won

#Make Bot stop a winning move
#Make Bot go for a winning move

#Make Bot Choose the best moves

'''
def bot_move(correct):
    #Compare a possible move to winning patterns
    
    
    #Make a pattern that goes (X)(X)(None)

    #if decide = None, then keep choosing random choices
    # if decide = 1, then just choose any random available choice and input it 

    decide = correct

    bot_available_choices = available_choices
    
    final_choice = bot_choice
    test_choice = random.choice(bot_available_choices)

    out_of_choices = []

    for i in range(1, int(len(bot_available_choices)) + 1):
        if bot_choice == 1:
            match_input(test_choice, bot_side, 0)
            win_conditioner()
            bot_available_choices.remove(test_choice)
            test_choice = random.choice(bot_available_choices)
            board[0][0] = None
        elif bot_choice == 2:
            match_input(test_choice, bot_side, 0)
            win_conditioner()
            bot_available_choices.remove(test_choice)
            test_choice = random.choice(bot_available_choices)
            board[0][1] = None
        elif bot_choice == 3:
            match_input(test_choice, bot_side, 0)
            win_conditioner()
            bot_available_choices.remove(test_choice)
            test_choice = random.choice(bot_available_choices)
            board[0][2] = None
        elif bot_choice == 4:
            match_input(test_choice, bot_side, 0)
            win_conditioner()
            bot_available_choices.remove(test_choice)
            test_choice = random.choice(bot_available_choices)
            board[1][0] = None
        elif bot_choice == 5:
            match_input(test_choice, bot_side, 0)
            win_conditioner()
            bot_available_choices.remove(test_choice)
            test_choice = random.choice(bot_available_choices)
            board[1][1] = None
        elif bot_choice == 6:
            match_input(test_choice, bot_side, 0)
            win_conditioner()
            bot_available_choices.remove(test_choice)
            test_choice = random.choice(bot_available_choices)
            board[1][2] = None
        elif bot_choice == 7:
            match_input(test_choice, bot_side, 0)
            win_conditioner()
            bot_available_choices.remove(test_choice)
            test_choice = random.choice(bot_available_choices)
            board[2][0] = None
        elif bot_choice == 8:
            match_input(test_choice, bot_side, 0)
            win_conditioner()
            bot_available_choices.remove(test_choice)
            test_choice = random.choice(bot_available_choices)
            board[2][1] = None
        elif bot_choice == 9:
            match_input(test_choice, bot_side, 0)
            win_conditioner()
            bot_available_choices.remove(test_choice)
            test_choice = random.choice(bot_available_choices)
            board[2][2] = None

    bot_available_choices = available_choices
    final_choice = random.choice(bot_available_choices)
    
    return final_choice
    '''

while game_over == False:
    if versus_bot == False:
        x_input = int(input("Player X Input: "))
        while x_input not in available_choices:
             x_input = int(input("Option already taken, try another: "))
             
        match_input(x_input, 'X')

        win_conditioner()
        
        if game_over == False:
            o_input = int(input("Player O Input: "))

            while o_input not in available_choices and game_over == False:
                o_input = int(input("Option already taken, try another: "))
                
        match_input(o_input, 'O')
    
        win_conditioner()

    elif versus_bot == True:
        if player_side == 'X':
            x_input = int(input("Player X Input: "))
            while x_input not in available_choices:
                x_input = int(input("Option already taken, try another: "))

            match_input(x_input, player_side)
            win_conditioner()
            
            match_input(bot_choice, bot_side)
            win_conditioner()

        
        elif player_side == 'O':
            match_input(bot_choice, bot_side)
            win_conditioner()

            print_board(0, 1)

            o_input = int(input("Player O Input: "))
            while o_input not in available_choices and game_over == False:
                o_input = int(input("Option already taken, try another: "))

            match_input(o_input, player_side)
            win_conditioner()
    
    bot_choice = random.choice(available_choices)
    print_board(1, 1)

    


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



