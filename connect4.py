import os

turn = "R"
grid = [[".", ".", ".", ".", ".", ".", "."], # 0
        [".", ".", ".", ".", ".", ".", "."], # 1
        [".", ".", ".", ".", ".", ".", "."], # 2
        [".", ".", ".", ".", ".", ".", "."], # 3
        [".", ".", ".", ".", ".", ".", "."], # 4
        [".", ".", ".", ".", ".", ".", "."]] # 5


# runs the actual game
def main(grid, turn):
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
            break
        else:
            counter -= 1


os.system("cls")
print("Welcome To Connect 4!")
print("To Place Your Token, Enter An Integer Corresponding To The Column You Want To Place Your Token In.")
print("To Start, Press Enter.")
start = input()


main(grid, turn)