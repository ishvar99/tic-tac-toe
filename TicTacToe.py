from random import randint
test_board = [' ']*10
test_board[0]='#'


def display_board(board):

        print('\t\t\t|   |')
        print(f'\t\t  {board[1]}\t| {board[2]} | {board[3]}')
        print('\t\t\t|   |')
        print('\t\t -----------')
        print('\t\t\t|   |')
        print(f'\t\t  {board[4]}\t| {board[5]} | {board[6]}')
        print('\t\t\t|   |')
        print('\t\t -----------')
        print('\t\t\t|   |')
        print(f'\t\t  {board[7]}\t| {board[8]} | {board[9]}')
        print('\t\t\t|   |')


def player_input():
    player1=input("Choose a marker 'X' or '0'!")
    return player1


def place_marker(board,marker,position):
    board[position]=marker


def win_check(board,marker):
    if(board[1]==board[2]==board[3]==marker) or\
            (board[4]==board[5]==board[6]==marker) or\
            (board[7]==board[8]==board[9]==marker) or\
            (board[1]==board[5]==board[9]==marker) or\
            (board[1]==board[4]==board[7]==marker) or\
            (board[2]==board[5]==board[8]==marker) or\
            (board[3]==board[6]==board[9]==marker) or\
            (board[3]==board[5]==board[7]==marker):
        return True
    else:
        return False


def choose_first():
    result = randint(0, 1)
    if result == 0:
        return 'player1'
    else:
        return 'player2'


def space_check(board,position):
    if board[position] == ' ':
        return True
    return False


def full_board_check(board):
    if ' ' in board:
        return False

    return True


def player_choice(board):
    position=int(input('Please choose your position(1-9) number'))
    if space_check(board,position):
        return position
    else:
        print('position already occupied!')
        return -1


def replay():
    result=input('Do you wanna play again!')
    if result.lower() == 'y':
        return True
    elif result.lower() == 'n':
        return False
    else:
        print('Invalid Input!')


while True:
    print("Player1: Do you want to be 'X' or 'O' ")
    player1= player_input()
    player2='X' if player1=='O' else 'O'
    x=choose_first()
    marker=player1 if x=='player1' else player2
    print(f"{x} will go first!")
    result =input('Are you ready to play!(y/n)').lower()
    if result == 'y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if not full_board_check(test_board):
            position = player_choice(test_board)
            if position==-1:
                position=player_choice(test_board)
            place_marker(test_board, marker, position)
            marker = player1 if marker == player2 else player2
            display_board(test_board)
            if win_check(test_board, player1) or win_check(test_board, player2):
                print('Congratulations! You won the game!')
                game_on=False
        else:
            print('Game tied!')
            game_on=False
    if not replay():
        break






