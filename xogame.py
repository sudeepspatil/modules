import random

def display(board):
    print('   |   |')
    print('  ' +board[1] + '| ' +   board[2] + ' | ' + board[3])
    print('   |   |')
    print('============')
    print('   |   |')
    print('  ' +board[4] + '| ' +   board[5] + ' | ' + board[6])
    print('   |   |')
    print('============')
    print('   |   |')
    print('  ' +board[7] + '| ' +   board[8] + ' | ' + board[9])
    print('   |   |')

test_board = ['#','x','o','x','o','x','o','x','o','x']

def x_or_o():
    marker = ''
    while marker != 'x' and marker != 'o':
        marker = input("player1 : 'x' or 'o':")
    
    if marker == 'x':
        return ('x','o')
    else:
       return ('o','x')

    

def positions(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    return ((board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or 
    (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or 
    (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or 
    (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark))


def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'player1'
    else:
        return 'player2'

def space_check(board,position):
    return board[position] == ' '

def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_check(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose the position: (1-9)'))
    return position

def replay():
    choice = input('want to play again? yes or no')
    return choice == 'yes'

print('welcome to tic tac game')

while True:
    the_board = [' ']*10
    player1_marker,player2_marker = x_or_o()
    turn = choose_first()
    print(turn + ' goes first')

    play_game = input('ready to play? y or n: ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player1':
            display(the_board)

            position = player_check(the_board)

            positions(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display(the_board)
                print('player1 is won ')
                game_on = False
            else:
                if full_check(the_board):
                    display(the_board)
                    print('tie game ')
                    break
                else:
                    turn = 'player2'
        
        else:
            display(the_board)

            position = player_check(the_board)

            positions(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                display(the_board)
                print('player2 is won ')
                game_on = False
            else:
                if full_check(the_board):
                    display(the_board)
                    print('tie game ')
                    break
                else:
                    turn = 'player1'

    if not replay():
        break
