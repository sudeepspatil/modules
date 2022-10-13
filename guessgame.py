from random import shuffle

mylist = [' ','O',' ']

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("pick an number:'0','1' or '2'")
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print('wrong guess!')
        print(mylist)

mixedup = shuffle_list(mylist)

guess = player_guess()

check_guess(mixedup,guess)
