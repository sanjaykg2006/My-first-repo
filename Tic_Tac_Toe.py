#My first project on Github
#Tic-Tac-Toe

board = ['-','-','-','-','-','-','-','-','-']
player = 'x'
win = 0
winner = 'x'
flag = 0

def disp_board():
    for i in range(0, 9):
        print(" | " + board[i] + " | ", end=" ")
        if i == 2 or i == 5 or i == 8:
            print("\n")

def play():
    choice = input("Enter Y or N if you want to play the game or not: ")
    if choice.upper() == 'Y':
        print("Welcome to Tic-Tac-Toe")
        play_game()
    else:
        print("Bye :(")
        return False

def check_tie():
    for i in range(0, 9):
        if board[i] == '-':
            return False  # Still empty spots
    return True  # No empty spots = tie

def flip_player():
    global player
    if player == 'x':
        player = 'o'
    else:
        player = 'x'

def check_win():
    # Rows
    if board[0] == board[1] == board[2] != '-':
        print("The winner is player " + board[0])
    elif board[3] == board[4] == board[5] != '-':
        print("The winner is player " + board[3])
    elif board[6] == board[7] == board[8] != '-':
        print("The winner is player " + board[6])
    # Columns
    elif board[0] == board[3] == board[6] != '-':
        print("The winner is player " + board[0])
    elif board[1] == board[4] == board[7] != '-':
        print("The winner is player " + board[1])
    elif board[2] == board[5] == board[8] != '-':
        print("The winner is player " + board[2])
    # Diagonals
    elif board[0] == board[4] == board[8] != '-':
        print("The winner is player " + board[0])
    elif board[2] == board[4] == board[6] != '-':
        print("The winner is player " + board[2])
    else:
        return False  # No winner yet
    print("Thank you for playing!")
    print("See you next time!")
    return True

def play_game():
    global player
    disp_board()
    print(player + " — It is your turn")
    
    try:
        ch = int(input("Enter a number between 0-8 to choose your place: "))
        if ch < 0 or ch > 8:
            print("Invalid input. Try again.")
            play_game()
            return
    except ValueError:
        print("Invalid input. Enter a number.")
        play_game()
        return

    if board[ch] == '-':
        board[ch] = player
    else:
        print("Spot already taken. Try again.")
        play_game()
        return

    if check_win():
        return
    elif check_tie():
        disp_board()
        print("The game is a tie.")
        print("Thank you for playing!")
        return
    else:
        flip_player()
        play_game()

play()

