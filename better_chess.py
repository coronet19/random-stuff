import os

board = [["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "  ", "  ", "WQ", "WK", "  ", "  ", "WR"]]

pieces = ["WP", "WR", "WN", "WB", "WK", "WQ", "BP", "BR", "BN", "BB", "BK", "BQ"]
white_pieces = ["WP", "WR", "WN", "WB", "WK", "WQ"]
black_pieces = ["BP", "BR", "BN", "BB", "BK", "BQ"]
white_en_passant_list = []
black_en_passant_list = []
error_list = []
move_repetition = []

castle_methods = ["O-O-O", "long castle", "O-O", "short castle"]
left_br_moved = False
bk_moved = False
right_br_moved = False
left_wr_moved = False
wk_moved = False
right_wr_moved = False

turn = "white"


#
#
#   Piece Moves
#
#


def rook_moveset(move):
    if is_killable(move) == False:
        error_list.append("Invalid Move: Piece In Intended Location Is Not Killable")
        return False
    if move[0] == move[-2]:
        start = reverse_int_index(move[1])
        end = reverse_int_index(move[-1])
        if abs(start - end) == 1: return True
        if start > end:
            temp = start
            start = end
            end = temp
        for i in range(start + 1, end):
            if board[i][reverse_alpha_index(move[0])] in pieces:
                error_list.append("Invalid Move: Piece Collision Occurance")
                return False
        return True
    elif move[1] == move[-1]:
        start_rank = reverse_int_index(move[1])
        start = reverse_alpha_index(move[0])
        end = reverse_alpha_index(move[-2])
        if abs(start - end) == 1: return True
        if start > end:
            temp = start
            start = end
            end = temp
        for i in range(start + 1, end):
            print(i)
            if board[start_rank][i] in pieces:
                error_list.append("Invalid Move: Piece Collision Occurance")
                return False
        return True
    error_list.append("Invalid Move: Intended Location Not In Valid Piece Moveset")
    return False


def bishop_moveset(move):
    if is_killable(move) == False:
        error_list.append("Invalid Move: Piece In Intended Location Is Not Killable")
        return False
    else:
        error_list.append("is killable")
        start = reverse_alpha_index(move[0])    
        end = reverse_alpha_index(move[-2])     
        row_start = reverse_int_index(move[1])  
        row_end = reverse_int_index(move[-1])   

        if abs(start - end) != abs(row_start - row_end):
            error_list.append("Invalid Move: Move Not In Valid Piece Moveset")
            return False

        if start > end:
            temp = start
            start = end
            end = temp

        for i in range(start + 1, end):
            if row_start < row_end:
                temp = row_start
                row_start = row_end
                row_end = temp
            print(2)
            if board[row_start - 1][i] in pieces:   
                error_list.append("Invalid Move: Piece Collision Detected")
                return False
            row_start -= 1
            continue
        return True


def knight_moveset(move):
    if is_killable(move) == False:
        error_list.append("Invalid Move: Piece In Intended Location Is Not Killable")
        return False
    if abs(int(move[1]) - int(move[-1])) == 2:
        if abs(reverse_alpha_index(move[0]) - reverse_alpha_index(move[-2])) == 1:
            return True
    elif abs(int(move[1]) - int(move[-1])) == 1:
        if abs(reverse_alpha_index(move[0]) - reverse_alpha_index(move[-2])) == 2:
            return True
    error_list.append("Invalid Move: Intended Location Not In Valid Piece Moveset")
    return False


def king_moveset(move):
    if is_killable(move) == False:
        error_list.append("Invalid Move: Piece In Intended Location Is Not Killable")
        return False
    if abs(reverse_alpha_index(move[0]) - reverse_alpha_index(move[-2])) <= 1:
        if abs(int(move[1]) - int(move[-1])) <= 1:
            return True
    error_list.append("Invalid Move: Intended Location Not In Valid Piece Moveset")
    return False


def white_pawn_moveset(move):
    if get_piece(move[-2:]) in pieces:
        if int(move[-1]) - int(move[1]) == 1:
            if is_killable(move):
                if abs(reverse_alpha_index(move[0]) - reverse_alpha_index(move[-2])) == 1:
                    return True
            if move[0] == move[-2]:
                error_list.append("Invalid Move: Piece In Intended Location Is Not Killable")
                return False
    elif get_piece(move[-2:]) not in pieces:
        if int(move[-1]) - int(move[1]) == 1:
            if get_piece(move[-2:]) in black_en_passant_list:
                if abs(reverse_alpha_index(move[0]) - reverse_alpha_index(move[-2])) == 1:
                    board[3][reverse_alpha_index(move[-2])] = "  "
                    return True
            elif move[0] == move[-2]:
                return True
        elif int(move[1]) == 2 and int(move[-1]) == 4:
            if move[0] == move[-2]:
                if board[5][reverse_alpha_index(move[0])] not in pieces:
                    white_en_passant_list.append(board[5][reverse_alpha_index(move[0])])
                    return True
                else:
                    error_list.append("Invalid Move: Piece Collision Detected")
                    return False
    error_list.append("Invalid Move: Intended Location Not In Valid Piece Moveset")
    return False


def black_pawn_moveset(move):
    if get_piece(move[-2:]) in pieces:
        if int(move[1]) - int(move[-1]) == 1:
            if is_killable(move):
                if abs(reverse_alpha_index(move[0]) - reverse_alpha_index(move[-2])) == 1:
                    return True
            if move[0] == move[-2]:
                error_list.append("Invalid Move: Piece In Intended Location Is Not Killable")
                return False
    elif get_piece(move[-2:]) not in pieces:
        if int(move[1]) - int(move[-1]) == 1:
            if get_piece(move[-2:]) in white_en_passant_list:
                if abs(reverse_alpha_index(move[-2]) - reverse_alpha_index(move[0])) == 1:
                    board[4][reverse_alpha_index(move[-2])] = "  "
                    return True
            elif move[0] == move[-2]:
                return True
        elif int(move[1]) == 7 and int(move[-1]) == 5:
            if move[0] == move[-2]:
                if board[2][reverse_alpha_index(move[0])] not in pieces:
                    black_en_passant_list.append(board[2][reverse_alpha_index(move[0])])
                    return True
                else:
                    error_list.append("Invalid Move: Piece Collision Detected")
                    return False
    error_list.append("Invalid Move: Intended Location Not In Valid Piece Moveset")
    return False

#
#
#   Utility Functions
#
#

# converts tile file to a board child index
def reverse_alpha_index(letter):
    return ord(letter) - 65

# converts tile rank to a board parent index
def reverse_int_index(number):
    return abs(int(number) - 8)

# gets the piece at a tile location
def get_piece(piece):
    return board[reverse_int_index(int(piece[1]))][reverse_alpha_index(piece[0])]

# checks piece being moved and its intended location, returns false if pieces at both locations are the same color
def is_killable(move):
    if get_piece(move[:2]) in white_pieces:
        if get_piece(move[-2:]) not in white_pieces:
            return True
    elif get_piece(move[:2]) in black_pieces:
        if get_piece(move[-2:]) not in black_pieces:
            return True
    return False

# checks movesets of pieces
def is_valid(move):
    global error_list
    piece = get_piece(move[:2])
    if turn == "white":
        if piece == "WR":
            return rook_moveset(move)
        elif piece == "WB": return bishop_moveset(move) 
        elif piece == "WN": return knight_moveset(move)
        elif piece == "WQ":
            if rook_moveset(move) == True or bishop_moveset(move) == True:
                error_list = []
                return True
            else:
                if "Invalid Move: Piece In Intended Location Is Not Killable" in error_list:
                    error_list = ["Invalid Move: Piece In Intended Location Is Not Killable"]
                elif "Invalid Move: Piece Collision Detected" in error_list:
                    error_list = ["Invalid Move: Piece Collision Detected"]
                elif "Invalid Move: Intended Location Not In Valid Piece Moveset" in error_list:
                    error_list = ["Invalid Move: Intended Location Not In Valid Piece Moveset"]
        elif piece == "WK": return king_moveset(move)
        elif piece == "WP": return white_pawn_moveset(move)
    elif turn == "black":
        if piece == "BR": return rook_moveset(move)
        elif piece == "BB": return bishop_moveset(move)
        elif piece == "BN": return knight_moveset(move)
        elif piece == "BQ":
            if rook_moveset(move) == True or bishop_moveset(move) == True:
                error_list = []
                return True
        elif piece == "BK": return king_moveset(move)
        elif piece == "BP": return black_pawn_moveset(move)
    return False

def pawn_promotion():
    valid_promotions = ["rook", "knight", "bishop", "queen"]
    for tile in board[0]:
        if tile == "WP":
            while True:
                tile_index = board[0].index("WP")
                os.system("cls")
                print_board()
                promotion = input("What Piece Do You Want To Promote To?\nRook, Knight, Bishop, or Queen? ")
                if promotion.strip().lower() in valid_promotions:
                    board[0][tile_index] = "W" + promotion[0].upper()
                    break
    for tile in board[7]:
        if tile == "BP":
            while True:
                promotion = input("What Piece Do You Want To Promote To?\nRook, Knight, Bishop, or Queen? ")
                if promotion.lower().strip() in valid_promotions:
                    tile = "B" + promotion[0].upper()
                    break
            break


def repetition_checker():
    if len(move_repetition) > 8:
        if move_repetition[:4] == move_repetition[4:8]:
            if move_repetition[8] == move_repetition[0]:
                return True
        move_repetition.pop(0)

def has_moved(color, castle_type):
    if color == "white":
        if wk_moved == True: return True
        if castle_type == "long":
            pass
        elif castle_type == "short":
            pass
    if color == "black":
        if castle_type == "long":
            pass
        elif castle_type == "short":
            pass

def castle(move, turn):
    if move in castle_methods[:2]:
        if turn == "white":
            if board[7][1:4] != ["  ", "  ", "  "]: return False
            if has_moved("white", "long"): return False
        elif turn == "black":
            if board[0][1:4] != ["  ", "  ", "  "]: return False
            if has_moved("black", "long"): return False

    elif move in castle_methods[3:]:
        if turn == "white":
            if board[7][5:7] != ["  ", "  "]: return False
            if has_moved("white", "short"): return False
        elif turn == "black":
            if board[0][5:7] != ["  ", "  "]: return False
            if has_moved("black", "short"): return False

    return True

# updates displayed board
def update_board(move):
    global turn
    global error_list
    error_list = []

    if move in castle_methods:
        if castle(move, turn) == False:
            error_list.append("Invalid Move: Castle Not Available")
        else:
            return True

    board[reverse_int_index(move[-1])][reverse_alpha_index(move[-2])] = get_piece(move[:2])
    board[reverse_int_index(move[1])][reverse_alpha_index(move[0])] = "  "


# displays board
def print_board(turn):
    if turn == "white":
        count = 9
        for row in board:
            count -= 1
            print(str(count) + "  ", end="")
            for tile in row:
                if tile == "":
                    print("  ", end="")
                print(tile, end=" ")
            if board.index(row) < 7:
                print("")
        print("\n   A  B  C  D  E  F  G  H")
    else:
        reverse_board = [board[7], board[6], board[5], board[4], board[3], board[2], board[1], board[0]]
        count = 0
        for row in reverse_board:
            count += 1
            print(str(count) + "  ", end="")
            for tile in row:
                if tile == "":
                    print("  ", end="")
                print(tile, end=" ")
            if count > 1:
                print("")
        print("\n   H  G  F  E  D  C  B  A")



# runs the program
while True:
    try:
        # checks for pawn promotion and promotes pawns
        pawn_promotion()

        # moves are being repeated, draws the game
        if repetition_checker():
            print("Draw By Repetition")
            break

        # clears terminal
        os.system("cls")
        #print("\n" * 5)

        # prints the chess board
        print_board(turn)

        # prints errors from previous move
        if error_list != []:
            for item in error_list:
                print(item)
            error_list = []

        # checks if it is whites turn
        if turn == "white":

            # asks user for input
            move = input("White To Move: ").upper().strip()

            # resets what black can use as en passant
            white_en_passant_list = []

            #remove this
            if move == "PASS":
                turn = "black"
                continue

            # checks if user wishes to resign
            if move == "RESIGN":
                print("Black Wins")
                break

            if move in castle_methods:
                castle(move)

            # checks if a piece has been selected
            if get_piece(move[:2]) not in pieces:
                error_list.append("Invalid Move: No Piece Selected")
                continue

            # checks if the move is valid, then updates board
            if is_valid(move):
                move_repetition.append(move)
                update_board(move)
                turn = "black"
                continue

        elif turn == "black":
            move = input("Black To Move: ").upper()
            black_en_passant_list = []
            if move == "PASS":
                turn = "white"
                continue

            elif move == "RESIGN":
                print("White Wins")
                break

            elif is_valid(move):
                move_repetition.append(move)
                update_board(move)
                turn = "white"
                continue

    except: continue
    else: continue




# make sure to add these
#
#   castling
#
#
#   create check checker
#   take location of kings and run it through is_valid() for every piece on board



# for castle shiz
#
# put below function at end of is_valid(move) function
# if get_piece(move[:2]) in ["WR", "WK", "BR", "BK"]:
#     update_castle_methods(move)
#
# update_castle_methods(move) will update valid castling directions
#
# possible update_castle_methods() code
# if
#
# when user castles, check if castle direction is valid, then if you even can castle