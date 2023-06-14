prompt_1 = "Please enter the board size\n"
prompt_2 = "Please enter how many squares you want to place\n"
prompt_3 = "Please enter the coordinates of a square you want to place\n"
prompt_4 = "Please enter a target square coordinate, or enter exit to exit\n"
prompt_5 = "Congratulations, you won!"
prompt_6 = "Thanks for playing."
error_message_1 = "Improper board size"
error_message_2 = "Improper amount of squares"
error_message_3 = "Incorrect input format for square coordinates"
error_message_4 = "Improper square coordinates"
error_message_5 = "Sign already placed to square"

print("Welcome to the +X- Game !")

size = int(input(prompt_1))
board = []


# Function for creating the game board with all squares having "-" sign
def board_generator(board_size):
    board_row = ""
    for i in range(1, board_size + 2):
        if i == 1:
            board_row = board_row + "  "
            for k in range(1, board_size + 1):
                board_row = board_row + str(k) + " "
            board_row = board_row[:-1]
            board.append(board_row)
        else:
            board_row = board_row + str(i - 1)
            for k in range(board_size):
                board_row = board_row + " -"
            board.append(board_row)
        board_row = ""
    return board


def board_printer(board_list):
    for k in board_list:
        print(k)


# Check if the board size is between 5 and 9
while size not in range(5, 10):
    print(error_message_1)
    size = int(input(prompt_1))

board_generator(size)
square_count = int(input(prompt_2))  # Amount of "+" signs the player wants to add to the board

# Player cannot place "+" signs more than the number of squares available on the board
while square_count not in range(1, (size ** 2) + 1):
    print(error_message_2)
    square_count = int(input(prompt_2))


# Function for replacing "-" sign with "+" sign
def replace_with_square(board):
    try:
        square_string = input(prompt_3).strip()
        if square_string.lower() == "exit":
            return "exit"
        square_list = square_string.split()
        x_coordinate = int(square_list[0])
        y_coordinate = int(square_list[1])
        if x_coordinate < 1 or x_coordinate > size or y_coordinate < 1 or y_coordinate > size:  # Out of board borders
            print(error_message_4)
            return "error message 4"
        else:
            if board[x_coordinate][2 * y_coordinate] == "+":  # Sign already replaced
                print(error_message_5)
                return "error message 5"
            else:  # Replace the square with "+" by modifying the line
                board[x_coordinate] = board[x_coordinate][: 2 * y_coordinate] + "+" + board[x_coordinate][2 * y_coordinate + 1:]
                return "success"
    except:  # Incorrect input format
        print(error_message_3)
        return "error message 3"


# Place "+" signs on the board
for i in range(square_count):
    while True:
        error_or_success = replace_with_square(board)
        if error_or_success == "success":
            break
        elif error_or_success == "exit":
            print(prompt_6)
            quit()
    board_printer(board)


# Choose squares to replace with "-"
def choose_target(board):
    try:
        target_inp = input(prompt_4).strip()
        if target_inp.lower() == "exit":
            return "exit"
        else:
            target_list = target_inp.split()
            target_x = int(target_list[0])  # Get the x-coordinate of the target square
            target_y = int(target_list[1])  # Get the y-coordinate of the target square
            if target_x < 1 or target_x > size or target_y < 1 or target_y > size:  # Out of board boundaries
                print(error_message_4)
                return "error message 4"
            else:
                if board[target_x][2 * target_y] == "+":
                    board[target_x] = board[target_x][:2 * target_y] + "-" + board[target_x][2 * target_y + 1:]
                else:  # If the sign at the target square is "-" it will convert into "+" sign
                    board[target_x] = board[target_x][:2 * target_y] + "+" + board[target_x][2 * target_y + 1:]
                if target_y != 1 and target_x != 1:
                    if board[target_x - 1][2 * (target_y - 1)] == "+":  # Change upper left corner of the target square
                        board[target_x - 1] = board[target_x - 1][:2 * (target_y - 1)] + "-" + board[target_x - 1][2 * target_y - 1:]
                    else:
                        board[target_x - 1] = board[target_x - 1][:2 * (target_y - 1)] + "+" + board[target_x - 1][2 * target_y - 1:]
                if target_y != size and target_x != 1:
                    if board[target_x - 1][2 * (target_y + 1)] == "+":  # Change upper right corner of the target square
                        board[target_x - 1] = board[target_x - 1][:2 * (target_y + 1)] + "-" + board[target_x - 1][2 * target_y + 3:]
                    else:
                        board[target_x - 1] = board[target_x - 1][:2 * (target_y + 1)] + "+" + board[target_x - 1][2 * target_y + 3:]
                if target_y != 1 and target_x != size:
                    if board[target_x + 1][2 * (target_y - 1)] == "+":  # Change lower left corner of the target square
                        board[target_x + 1] = board[target_x + 1][:2 * (target_y - 1)] + "-" + board[target_x + 1][2 * target_y - 1:]
                    else:
                        board[target_x + 1] = board[target_x + 1][:2 * (target_y - 1)] + "+" + board[target_x + 1][2 * target_y - 1:]
                if target_y != size and target_x != size:
                    if board[target_x + 1][2 * (target_y + 1)] == "+":  # Change lower right corner of the target square
                        board[target_x + 1] = board[target_x + 1][:2 * (target_y + 1)] + "-" + board[target_x + 1][2 * target_y + 3:]
                    else:
                        board[target_x + 1] = board[target_x + 1][:2 * (target_y + 1)] + "+" + board[target_x + 1][2 * target_y + 3:]
                return board
    except:  # Incorrect input format
        print(error_message_3)
        return "error message 3"


# Calculate the amount of "+" signs on the board
def plus_counter(board):
    plus_count = 0
    for row in board:
        for ch in row:
            if ch == "+":
                plus_count += 1
    return plus_count


plus_count = plus_counter(board)

while plus_count > 0:  # Game will continue until all "+" signs are converted to "-" or player types "exit"
    while True:
        error_or_okay_target = choose_target(board)
        if error_or_okay_target != "error message 3" and error_or_okay_target != "error message 4":
            break
    if error_or_okay_target == "exit":
        break
    board_printer(board)
    plus_count = plus_counter(board)

if plus_count == 0:  # Player wins
    print(prompt_5)

print(prompt_6)
