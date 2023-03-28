import os

turn = "R"
grid = [[".", ".", ".", ".", ".", ".", "."], # 0
        [".", ".", ".", ".", ".", ".", "."], # 1
        [".", ".", ".", ".", ".", ".", "."], # 2
        [".", ".", ".", ".", ".", ".", "."], # 3
        [".", ".", ".", ".", ".", ".", "."], # 4
        [".", ".", ".", ".", ".", ".", "."]] # 5
grid_checklist = []


# updates the list used to check for all possible winning scenarios
def update_checklist():
    global grid_checklist           # vertical
    grid_checklist = [[grid[0][0], grid[1][0], grid[2][0], grid[3][0], grid[4][0], grid[5][0]],
                    [grid[0][1], grid[1][1], grid[2][1], grid[3][1], grid[4][1], grid[5][1]],
                    [grid[0][2], grid[1][2], grid[2][2], grid[3][2], grid[4][2], grid[5][2]],
                    [grid[0][3], grid[1][3], grid[2][3], grid[3][3], grid[4][3], grid[5][3]],
                    [grid[0][4], grid[1][4], grid[2][4], grid[3][4], grid[4][4], grid[5][4]],
                    [grid[0][5], grid[1][5], grid[2][5], grid[3][5], grid[4][5], grid[5][5]],
                    [grid[0][6], grid[1][6], grid[2][6], grid[3][6], grid[4][6], grid[5][6]],
                    # down, right
                    [grid[0][3], grid[1][4], grid[2][5], grid[3][6]],
                    [grid[0][2], grid[1][3], grid[2][4], grid[3][5], grid[4][6]],
                    [grid[0][1], grid[1][2], grid[2][3], grid[3][4], grid[4][5], grid[5][6]],
                    [grid[0][0], grid[1][1], grid[2][2], grid[3][3], grid[4][4], grid[5][5]],
                    [grid[1][0], grid[2][1], grid[3][2], grid[4][3], grid[5][4]],
                    [grid[2][0], grid[3][1], grid[4][2], grid[5][3]],
                    # down, left / up, right
                    [grid[3][0], grid[2][1], grid[1][2], grid[0][3]],
                    [grid[4][0], grid[3][1], grid[2][2], grid[1][3], grid[0][4]],
                    [grid[5][0], grid[4][1], grid[3][2], grid[2][3], grid[1][4], grid[0][5]],
                    [grid[5][1], grid[4][2], grid[3][3], grid[2][4], grid[1][5], grid[0][6]],
                    [grid[5][2], grid[4][3], grid[3][4], grid[2][5], grid[1][6]],
                    [grid[5][3], grid[4][4], grid[3][5], grid[2][6]]]


# runs the actual game
def main():
    global grid
    global turn
    while True:
        try:
            print_grid()
            if turn == "R":
                column = int(input("Red's Turn: ").strip())
                if grid[0][column - 1] != ".":
                    continue
                update_board(column)
                if win_checker("R") == True:
                    print_grid()
                    print("Red Wins!")
                    break
                turn = "B"
            elif turn == "B":
                column = int(input("Blue's Turn: ").strip())
                if grid[0][column - 1] != ".":
                    continue
                update_board(column)
                if win_checker("B") == True:
                    print_grid()
                    print("Blue Wins!")
                    break
                turn = "R"
        except: continue
        else: continue


# checks for every possible win scenario
def win_checker(turn):
    global grid
    global grid_checklist
    for row in grid_checklist:
        counter = 0
        while counter <= len(row) - 4:
            checklist = [row[counter], row[counter + 1], row[counter + 2], row[counter + 3]]
            if checklist == [turn, turn, turn, turn]:
                return True
            else:
                counter += 1
                continue
    for row in grid:
        counter = 0
        while counter <= len(row) - 4:
            checklist = [row[counter], row[counter + 1], row[counter + 2], row[counter + 3]]
            if checklist == [turn, turn, turn, turn]:
                return True
            else:
                counter += 1
                continue
    return False


# displays the connect 4 board/grid
def print_grid():
    os.system("cls")
    for row in grid:
        for tile in row:
            print(tile, end="  ")
        print("")
    for i in range(1, 8):
        print(i, end="  ")
    print("")


# places users token on the board
def update_board(move):
    column = move - 1
    counter = len(grid) - 1
    while counter >= 0:
        if grid[counter][column] == ".":
            grid[counter][column] = turn
            update_checklist()
            break
        else:
            counter -= 1

os.system("clear")
print("Welcome To Connect 4!")
print("To Place Your Token, Enter An Integer Corresponding To The Column You Want To Place Your Token In.")
print("To Start, Press Enter.")
start = input()


main()