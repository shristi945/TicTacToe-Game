#--------Global Variables-------

#to check if game is still running  
game_still_on = True

# to set the current player playing
current_player = "X"

# to who is the winner?
winner = None

# Initial Board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#to display board
def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])
    
# main working function 
def play_game():
    
    #to display initial the board
    display_board()
    
    # loop to run every time till the game is on
    while game_still_on:
        
        
        handle_turn(current_player)
        
        display_board()
        
        check_to_continue()
        
        flip_player()
    
# function to ask input and validate it before setting it on board
def handle_turn(player):
    
    #input a position
    position = input("choose a position from the board cell 1-9:")
    
    # if user inputs anything other than a digit -- invalid input
    if position.isdigit()== False:
        print("Please input a cell number")
        return
    else:
        position = int(position)-1
    
    #if user inputs anything more than 9 or less than 1 -- invalid input 
    if position<0 or position>8:
        print("Please input a number between 1-9 ")
        return
    
    #if user inputs already filled cell with X or 0 -- invalid move
    if board[position]== 'X' or board[position] == '0':
        print("Position already taken")
        return
    else:
        # placing the player sign for valid move and position value
        board[position]=player
    
# to check if we can continue the game while there is no winner or no tie
def check_to_continue():
    # check win
    check_winner()
    # check if tie
    check_tie()
    
#to check and print if Won
def check_winner():
    
    #global variables
    global winner
    global game_still_on
    #check row
    row_win = check_row()
    #check column
    column_win = check_column()
    #check diagonals 
    diagonal_win = check_diagonals()
    
    if row_win:
        winner = row_win
    elif column_win:
        winner = column_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None
        return

    if winner == "X":
        game_still_on = False
        print("X Won!")
    if winner == "0":
        game_still_on = False
        print("0 Won!")
    
#to check all the three rows    
def check_row():
    
    row_1 = board[0]==board[1]==board[2]!='-'
    row_2 = board[3]==board[4]==board[5]!='-'
    row_3 = board[6]==board[7]==board[8]!='-'
    
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

#to check all the three columns
def check_column():
    column_1 = board[0]==board[3]==board[6]!='-'
    column_2 = board[1]==board[4]==board[7]!='-'
    column_3 = board[2]==board[5]==board[8]!='-'
    
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

#to check all the two diagonals
def check_diagonals():
    diagonal_1 = board[0]==board[4]==board[8]!='-'
    diagonal_2 = board[6]==board[4]==board[2]!='-'

    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]
    return

#to check if there is a tie in the board
def check_tie():
    
    #global Variable
    global game_still_on
    if "-" not in board:
        game_still_on = False
        print("Its a Tie")
    return

#to change turns between player
def flip_player():
    
    #global variable
    global current_player
    
    if current_player == 'X':
        current_player = '0'
    elif current_player == '0':
        current_player='X'
    return     

#calling the main working function to start the game
play_game()    