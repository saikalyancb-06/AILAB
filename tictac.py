import math

HUMAN = 'X'
COMPUTER = 'O'
EMPTY = ' '

def print_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---+---+---")
    print()

def check_win(board, player):
    win_states = [[0,1,2],[3, 4, 5], [6, 7, 8],
     [1, 4, 7], [2, 5, 8],[0,3,6],
     [2, 4, 6],[0,4,8]
    ]
    for condition in win_states:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    return EMPTY not in board

def minimax(board, depth, is_maximizing):
    if check_win(board, COMPUTER):
        return 1
    if check_win(board, HUMAN):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = COMPUTER
                score = minimax(board, depth + 1, False)
                board[i] = EMPTY
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(board, depth + 1, True)
                board[i] = EMPTY
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = COMPUTER
            score = minimax(board, 0, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [EMPTY] * 9
    print("Welcome to Tic-Tac-Toe!\n")
    print_board(board)
    
    while True:
        while True:
            try:
                move = int(input("Human Player (X) - Choose position (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == EMPTY:
                    board[move] = HUMAN
                    break
                else:
                    print("Invalid move. Position already filled or out of bounds.")
            except ValueError:
                print("Please enter a valid integer between 1 and 9.")
        
        print("\n--- Current Board State ---")
        print_board(board)
        
        if check_win(board, HUMAN):
            print("Human Player Wins")
            break
            
        if is_board_full(board):
            print("Game Draw")
            break
            
        print("Computer Player (O) is calculating move...")
        comp_move = find_best_move(board)
        board[comp_move] = COMPUTER
        print_board(board)
        
        if check_win(board, COMPUTER):
            print("Computer Player Wins")
            break
            
        if is_board_full(board):
            print("Game Draw")
            break

if __name__ == '__main__':
    play_game()
