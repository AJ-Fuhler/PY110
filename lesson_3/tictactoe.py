import random
import os
import time

INITIAL_MARKER = ' '
USER_MARKER = 'X'
COMPUTER_MARKER = 'O'
NR_GAMES_TO_WIN_MATCH = 5
VALID_START_OPTIONS = ['player', 'computer', 'choose']

WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # colums
        [1, 5, 9], [3, 5, 7]             # diagonals
    ]

def prompt(message):
    print(f'==> {message}')

def display_board(board):

    prompt(f'You are {USER_MARKER}. Computer is {COMPUTER_MARKER}.')
    print('')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')
    print('')


def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key
            for key, value in board.items()
            if value == INITIAL_MARKER]

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square ({join_or(valid_choices)}):')
        square = input().strip()
        if square in valid_choices:
            break
        
        prompt('That is not a valid choice.')

    
    board[int(square)] = USER_MARKER

def join_or(lst, delimiter=', ', final_delimiter='or'):
    result = ''
    
    for element in lst[:-2]:
        result += f'{element}{delimiter}'
    if len(lst) > 1:
        result += f'{lst[-2]} {final_delimiter} {lst[-1]}'
    elif len(lst) == 1:
        return str(lst[0])


    return result

def find_at_risk_square(line, board, marker):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = None
    for line in WINNING_LINES:
        square = find_at_risk_square(line, board, COMPUTER_MARKER)
        if square:
            break
    
    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(line, board, USER_MARKER)
            if square:
                break
    if not square:
        if board[5] == INITIAL_MARKER:
            square = 5
    
    if not square:
        square = random.choice(empty_squares(board))
    
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0 # or return not empty_squares(board)

def someone_won_round(board):
    return bool(detect_round_winner(board))

def detect_round_winner(board):

    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == USER_MARKER
            and board[sq2] == USER_MARKER
            and board[sq3] == USER_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
              and board[sq2] == COMPUTER_MARKER
              and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
        
    return None

def display_score(score):
    os.system('clear')
    print(f"You: {score['Player']} | Computer: {score['Computer']}")

def increment_score(score, board):
    score[detect_round_winner(board)] += 1

def detect_match_winner(score):
    if score['Player'] == NR_GAMES_TO_WIN_MATCH:
        return 'You'
    elif score['Computer'] == NR_GAMES_TO_WIN_MATCH:
        return 'Computer'
    
    return None

def someone_won_match(score):
    return bool(detect_match_winner(score))

def choose_square(board, current_player):
    if current_player == 'player':
        player_chooses_square(board)
    else:
        computer_chooses_square(board)

def alternate_player(current_player):
    if current_player == 'player':
        return 'computer'
    else:
        return 'player'
    
def choose_who_starts():
    prompt(f'Who do you want to start? {join_or(VALID_START_OPTIONS)}?')
    choice = input().strip().lower()
    while choice not in VALID_START_OPTIONS:
        prompt('Please choose a valid option')
        choice = input().strip().lower()

    if choice == 'choose':
        return random.choice(VALID_START_OPTIONS[:2])
    
    return choice

def get_valid_answer():
    answer = input().strip().lower()
    while answer not in ['y', 'n']:
        prompt('Please choose a valid option')
        answer = input().strip().lower()
    
    return answer


def play_tic_tac_toe():
    while True:
        score = {
            'Player': 0,
            'Computer': 0
        }
        while True:
            board = initialize_board()
            current_player = choose_who_starts()

            while True:
                display_score(score)
                display_board(board)
                choose_square(board, current_player)
                current_player = alternate_player(current_player)
                if someone_won_round(board) or board_full(board):
                    break

            display_score(score)            
            display_board(board)

            if someone_won_round(board):
                prompt(f'{detect_round_winner(board)} won this round!')
                increment_score(score, board)
                time.sleep(1.5)
            else:
                prompt("You tied this round!")
                time.sleep(2)
            
            if someone_won_match(score):
                break
            
        display_score(score)        
        prompt(f'{detect_match_winner(score)} won the match!')
        time.sleep(1)     
        prompt('Play again? (y or n)')
        answer = get_valid_answer()
        
        if answer[0] == 'n':
            break

    prompt('Thanks for playing Tic Tac Toe!')


play_tic_tac_toe()


