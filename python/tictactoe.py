import random

def drawboard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def playagain():
    print("Do you want to play again? (Y/N)")
    return input().lower().startswith('y')

def winner(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or 
    (board[4] == letter and board[5] == letter and board[6] == letter) or 
    (board[7] == letter and board[8] == letter and board[9] == letter) or 
    (board[1] == letter and board[4] == letter and board[7] == letter) or 
    (board[2] == letter and board[5] == letter and board[8] == letter) or 
    (board[3] == letter and board[6] == letter and board[9] == letter) or 
    (board[1] == letter and board[5] == letter and board[9] == letter) or 
    (board[7] == letter and board[5] == letter and board[3] == letter))

def move(board,letter,pos):
    board[pos]=letter

def spacefree(board,pos):
    if board[pos] == ' ':
        return True
    else:
        return False

def playermove(board):
    pos=' '
    while pos not in '1,2,3,4,5,6,7,8,9'.split(",") or spacefree(board, int(pos)) is False:
        print('Enter your next move (1-9)')
        pos=input()
    return int(pos)

def boardfull(board):
    #true=full false=not full
    for i in range(1, 10):
        if spacefree(board, i):
            return False

    return True

def computermove(board):
    pos = random.randint(0, 9)
    while spacefree(board, pos) is False:
	    pos=random.randint(0, 9)
    return int(pos)
	
while True:
    #resetsboard
    board = [' '] * 10
    gameplay = True
    print('You are X. You play first')
    turn='player'
    completter='O'
    playerletter='X'

    while gameplay:
        if turn == 'player':
            #playerplays
			
            drawboard(board)
            pos = playermove(board)
            move(board, playerletter, pos)

            if winner(board, playerletter):
                drawboard(board)
                print('You have won the game!')
                gameplay = False
            else:
                if boardfull(board):
                    drawboard(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            #computerplays
			
            pos = computermove(board)
            move(board, completter, pos)

            if winner(board, completter):
                drawboard(board)
                print('The computer won.')
                gameplay = False
            else:
                if boardfull(board):
                    drawboard(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playagain():
        break
