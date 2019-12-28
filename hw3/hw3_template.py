import random

N = 10
USER = 0
COMPUTER = 1
MAX_SIZE = 4

# a mapping from a ship size to the number of battleship of this size that need to be placed.
SHIP_SIZE_TO_COUNT = [0, 4, 3, 2, 1]

BATTLESHIP_MARK = '*'
MISS_MARK = 'X'
HIT_MARK = 'V'
EMPTY = ' '
HIT_CODE = 0
MISS_CODE = 1
INVALID_CODE = 2


def check_if_top_vertical(board, x, y):
    '''
    Check if board[y][x] is the top vertical part of the battleship
    :param board: a following table
    :param x: column coordinate
    :param y: row coordinate
    :return: True if the location is top vertical, else False.
    ''' 
    for j in range(x-1, max(x-MAX_SIZE, -1), -1):
        if board[y][j] not in [BATTLESHIP_MARK, HIT_MARK]:
            return True
        if board[y][j] == BATTLESHIP_MARK:
            return False

    return True


def check_if_top_horizontal(board, x, y):
    '''
    Check if board[y][x] is the top horizontal part of the battleship.
    :param board: a following table
    :param x: column coordinate
    :param y: row coordinate
    :return: True if the location is top horizontal, else False.
    ''' 
    for i in range(y - 1, max(y - MAX_SIZE, -1), -1):
        if board[i][x] not in [BATTLESHIP_MARK, HIT_MARK]:
            return True
        if board[i][x] == BATTLESHIP_MARK:
            return False

    return True


def count_battleships(board):
    '''
    Counts the number of battleships left on the table.
    :param board: a following table
    :return: The number of battleships.
    '''
    counter = 0
    num_rows = num_cols = N
    for i in range(num_rows):
        for j in range(num_cols):
            if board[i][j] != BATTLESHIP_MARK:
                continue
            if check_if_top_horizontal(board, j, i) and check_if_top_vertical(board, j, i):
                counter += 1
    return counter


def print_board(board, player):
    '''
    Prints the board which corresponds to the player.
    :param board: the players board
    :param player: the current player
    :return: 
    '''
    print('    ', end='')
    print(' '.join([str(row) for row in range(N)]))
    print('    ', end='')
    print(' '.join(['-' for _ in range(N)]))
    for row in range(0, N, 1):
        print(row, end=' | ')
        if player == COMPUTER:
            print(' '.join(board[row]).replace('*', ' '))
        else:
            print(' '.join(board[row]))

    print()


def print_game_status(user_board, computer_board):
    '''
    Prints the game status.
    :param user_board: the users board
    :param computer_board: the computers board
    :return: 
    '''
    print("Your following table:")
    print_board(computer_board,COMPUTER)
    print("The computer's following table:")
    print_board(user_board,USER)
    

def print_drown_battleship_message(player, count):
    '''
    Prints a message when a battleship has drown.
    :param player: the current player
    :param count: the count of battleships
    :return: 
    '''
    if player == USER :
        print("The computer's battleship has been drowned.")
    else :
        print("Your battleship has been drowned.")
    print(str(count)+"/10 battleships remain!")


def print_winner_message(player):
    '''
    Prints a message when the game is over
    :param player: the winner player
    :return: 
    '''
    if player == COMPUTER:
        print('Congrats! You are the winner :)')
    else:
        print('Game over! The computer won the fight :(')


def check_and_place_vertical_ship(board, x, y, size):
    '''

    Given the location and size, check if the parameters are valid and if so,
    place the battleship vertically.
    :param board: a board
    :param x: column coordinate
    :param y: row coordinate
    :param size: the size of the battleship
    :return: True if the battleship was placed, otherwise False.
    '''
    if y+size-1 >= N:
        return False
    most_left = max(0,x-1)
    most_right = min(N-1,x+1)
    most_up = max(0,y-1)
    most_down = min(N-1,y+size)
    # other ships check
    for i in range(most_up,most_down+1):
        for j in range(most_left,most_right+1):
            if board[i][j] != EMPTY :
                return False
    for i in range(y,y+size):
        board[i][x]=BATTLESHIP_MARK
    return True


def check_and_place_horizontal_ship(board, x, y, size):
    '''

    Given the location and size, check if the parameters are valid and if so,
    place the battleship horizontally.
    :param board: a board
    :param x: column coordinate
    :param y: row coordinate
    :param size: the size of the battleship
    :return: True if the battleship was placed, otherwise False.
    '''
    # can not place ship
    if x+size-1 >= N :
        return False
    # board frame check
    most_left = max(0,x-1)
    most_right = min(N-1,x+size)
    most_up = max(0,y-1)
    most_down = min(N-1,y+1)
    # other ships check
    for i in range(most_up,most_down+1):
        for j in range(most_left,most_right+1):
            if board[i][j] != EMPTY :
                return False
    #placing ship in the board
    for i in range(x,x+size):
        board[y][i]=BATTLESHIP_MARK
    return True



def check_location_and_place_ship(board, x, y, orientation, size):
    '''
    Given the location, size and orientation, check if the parameters are valid and if so,
    place it.
    :param board: a board
    :param x: column coordinate
    :param y: row coordinate
    :param orientation: the orientation of the battleship
    :param size: the size of the battleship
    :return: True if the battleship was placed, otherwise False.
    '''
    was_ship_placed = False
    if check_move(board,x,y)!= True:
        return False
    if orientation=='v':
        was_ship_placed = check_and_place_vertical_ship(board,x,y,size)
    else:
        was_ship_placed = check_and_place_horizontal_ship(board,x,y,size)
    return was_ship_placed



def initialize_and_set_board(player):
    '''
    Given a player, initialize an empty board and place all battleships.
    :param player: The current player.
    :return: The players board.
    '''
    board = []
    tmp_ship_size_to_count = [n for n in SHIP_SIZE_TO_COUNT]
    for i in range(N):
        board.append([EMPTY]*N)
    if player==USER : 
        print("Your current board:")
        print_board(board,USER)
        for size in range(1,len(tmp_ship_size_to_count)):
            while tmp_ship_size_to_count[size]!=0:
                print("Enter location for Battleship of size "+str(size)+":")
                user_input = input()
                orientation = user_input[-1]
                x = int(user_input.split(" ")[0].split(",")[0])
                y = int(user_input.split(" ")[0].split(",")[1])
                while check_location_and_place_ship(board,x,y,orientation,size)==False:
                    print("ERROR: Invalid location")
                    print("Please enter location for Battleship of size "+str(size)+" again:")
                    user_input = input()
                    orientation = user_input[-1]
                    x = int(user_input.split(" ")[0].split(",")[0])
                    y = int(user_input.split(" ")[0].split(",")[1])
                    continue
                else :
                    tmp_ship_size_to_count[size]-=1
                if size == len(tmp_ship_size_to_count)-1 and tmp_ship_size_to_count[size]==0:
                    continue
                print("Your current board:")
                print_board(board,USER)
    else :
        for size in range(1,len(tmp_ship_size_to_count)):
            while tmp_ship_size_to_count[size]!=0:
                x = random.randint(0,N-1)
                y = random.randint(0,N-1)
                orientation = random.randint(0,1)
                orientation = 'v' if orientation==1 else 'h'
                if check_location_and_place_ship(board,x,y,orientation,size)==False:
                    continue
                tmp_ship_size_to_count[size]-=1
    return board


def check_move(board, x, y):
    '''
    Given a following table and coordinates,
    check whether the move is legal.
    :param board:
    :param x: The column number.
    :param y: The row number.
    :return: True if the move is valid, else False.
    '''
    if x>=N or y>=N or x<0 or y<0:
        return False
    if board[y][x] not in [EMPTY,BATTLESHIP_MARK]:
        return False
    return True

def get_valid_computer_move(board):
    '''
    Randomize a valid move.
    :param board: The computer's following table.
    :return: a valid move
    '''
    x = random.randint(0,N-1)
    y = random.randint(0,N-1)
    while not check_move(board,x,y):
        x = random.randint(0,N-1)
        y = random.randint(0,N-1)
    return x,y


def get_valid_user_move(board):
    '''
    Scans a valid move from the user.
    :param board: The user's following table.
    :return: a valid move.
    '''
    print("It's your turn!")
    print("Enter location for attack:")
    user_input = input()
    x = int(user_input.split(",")[0])
    y = int(user_input.split(",")[1])
    while not check_move(board,x,y):
        print("Error: Invalid attack...")
        print("Please try again:")
        user_input = input()
        x = int(user_input.split(",")[0])
        y = int(user_input.split(",")[1])
    return x,y

def attack_location(board, player):
    '''
    Given a player and its following table,
    get valid location and attack it.
    :param board: The players following table.
    :param player: The current player.
    :return: Whether the attack was hit or miss.
    '''
    ships_left_before = count_battleships(board)
    if player == USER : 
        x,y = get_valid_user_move(board)
    else :
        x,y = get_valid_computer_move(board)
    if board[y][x] == EMPTY :
        board[y][x] = 'X'
    else :
        board[y][x]='V'
    ships_left_after = count_battleships(board)
    if ships_left_before!=ships_left_after:
        print_drown_battleship_message(player,ships_left_after)
    

def play_turn(board, player):
    '''

    :param board: NxN matrix representing the following table.
    :param player: The current player.
    :return: True whether game is still on, otherwise False.
    '''
    ships_left = count_battleships(board)
    if ships_left == 0:
        return False
    attack_location(board,player)
    ships_left = count_battleships(board)
    if ships_left == 0:
        return False
    return True



def main():
    print('Welcome to Battleship!')
    print('Please enter seed:')
    seed = int(input())
    random.seed(seed)

    # Initialize boards
    # ...
    p1_board = initialize_and_set_board(USER)
    computer_board = initialize_and_set_board(COMPUTER)
    #computer_board2 = initialize_and_set_board(COMPUTER)
    #print_board(computer_board,USER)
    #print_board(computer_board2,COMPUTER)
    print('All battleships have been located successfully!')
    # play game
    # ...
    i = 0
    play = True
    while play :
        if i == 0 :
            print_game_status(p1_board,computer_board)
            play = play_turn(computer_board,USER)
        else :
            play = play_turn(p1_board,COMPUTER)
        i=(i+1) % 2

    print_winner_message(i)



if __name__ == '__main__':
    main()
