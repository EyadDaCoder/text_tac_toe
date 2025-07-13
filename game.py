print("EyadDaCoder's tic tac toe engine: text_TO")
print("")

x_win = False
o_win = False
draw = False
played_moves_total = 0


# board data

ra = ["_", "_", "_"]
rb = ["_", "_", "_"]
rc = ["_", "_", "_"]

# underneath is a terrible way to edit the board data
def edit_board(row, box, player):
    global ra, rb, rc

    if row == "a" and int(box) == 1:
        if player == "X":
            ra[int(box) - 1] = player
        elif player == "O":
            ra[int(box) - 1] = player

    elif row == "a" and int(box) == 2:
        if player == "X":
            ra[int(box) - 1] = player
        elif player == "O":
            ra[int(box) - 1] = player

    elif row == "a" and int(box) == 3:
        if player == "X":
            ra[int(box) - 1] = player
        elif player == "O":
            ra[int(box) - 1] = player


    elif row == "b" and int(box) == 1:
        if player == "X":
            rb[int(box) - 1] = player
        elif player == "O":
            rb[int(box) - 1] = player

    elif row == "b" and int(box) == 2:
        if player == "X":
            rb[int(box) - 1] = player
        elif player == "O":
            rb[int(box) - 1] = player

    elif row == "b" and int(box) == 3:
        if player == "X":
            rb[int(box) - 1] = player
        elif player == "O":
            rb[int(box) - 1] = player


    elif row == "c" and int(box) == 1:
        if player == "X":
            rc[int(box) - 1] = player
        elif player == "O":
            rc[int(box) - 1] = player

    elif row == "c" and int(box) == 2:
        if player == "X":
            rc[int(box) - 1] = player
        elif player == "O":
            rc[int(box) - 1] = player

    elif row == "c" and int(box) == 3:
        if player == "X":
            rc[int(box) - 1] = player
        elif player == "O":
            rc[int(box) - 1] = player


# this checks for wins
def check_for_win():
    global x_win, o_win, draw, played_moves_total
    global ra, rb, rc

    # " X " Horizontal win check
    if ra[0] == "X" and ra[1] == "X" and ra[2] == "X":
        return "x_win"
    elif rb[0] == "X" and rb[1] == "X" and rb[2] == "X":
        return "x_win"
    elif rc[0] == "X" and rc[1] == "X" and rc[2] == "X":
        return "x_win"

    # " X " Vertical win check
    elif ra[0] == "X" and rb[0] == "X" and rc[0] == "X":
        return "x_win"
    elif ra[1] == "X" and rb[1] == "X" and rc[1] == "X":
        return "x_win"
    elif ra[2] == "X" and rb[2] == "X" and rc[2] == "X":
        return "x_win"

    # " X " Diagonal win check
    elif ra[0] == "X" and rb[1] == "X" and rc[2] == "X":
        return "x_win"
    elif rc[2] == "X" and rb[1] == "X" and ra[0] == "X":
        return "x_win"

    # " O " Horizontal win check
    elif ra[0] == "O" and ra[1] == "O" and ra[2] == "O":
        return "o_win"
    elif rb[0] == "O" and rb[1] == "O" and rb[2] == "O":
        return "o_win"
    elif rc[0] == "O" and rc[1] == "O" and rc[2] == "O":
        return "o_win"

    # " O " Vertical win check
    elif ra[0] == "O" and rb[0] == "O" and rc[0] == "O":
        return "o_win"
    elif ra[1] == "O" and rb[1] == "O" and rc[1] == "O":
        return "o_win"
    elif ra[2] == "O" and rb[2] == "O" and rc[2] == "O":
        return "o_win"

    # " O " Diagonal win check
    elif ra[0] == "O" and rb[1] == "O" and rc[2] == "O":
        return "o_win"
    elif rc[2] == "O" and rb[1] == "O" and ra[0] == "O":
        return "o_win"

    elif played_moves_total == 9:
        return "draw"
    else:
        pass


input("player x ready?")
input("player o ready?")
print("")
print("c |"+rc[0]+"|"+rc[1]+"|"+rc[2]+"|")
print("   ¹ ² ³")
print("b |"+rb[0]+"|"+rb[1]+"|"+rb[2]+"|")
print("   ¹ ² ³")
print("a |"+ra[0]+"|"+ra[1]+"|"+ra[2]+"|")
print("   ¹ ² ³")
print("")

#input loop
while True:
    if check_for_win() == "o_win":
        print("O Wins!")
        break
    elif check_for_win() == "draw":
        print("Its a draw! Nobody Wins!")
        break

    row_input_x = input("Player X turn! Enter the row letter: ")
    box_input_X = input("Now enter the box number: ")
    edit_board(row_input_x, box_input_X, "X")
    check_for_win()
    print("")
    print("c |" + rc[0] + "|" + rc[1] + "|" + rc[2] + "|")
    print("   ¹ ² ³")
    print("b |" + rb[0] + "|" + rb[1] + "|" + rb[2] + "|")
    print("   ¹ ² ³")
    print("a |" + ra[0] + "|" + ra[1] + "|" + ra[2] + "|")
    print("   ¹ ² ³")
    print("\n")
    print("")
    played_moves_total += 1

    if check_for_win() == "x_win":
        print("X Wins!")
        break
    elif check_for_win() == "draw":
        print("Its a draw! Nobody Wins!")
        break

    row_input_o = input("Player O turn! Enter the row letter: ")
    box_input_o = input("Now enter the box number: ")
    edit_board(row_input_o, box_input_o, "O")
    check_for_win()
    print("")
    print("c |" + rc[0] + "|" + rc[1] + "|" + rc[2] + "|")
    print("   ¹ ² ³")
    print("b |" + rb[0] + "|" + rb[1] + "|" + rb[2] + "|")
    print("   ¹ ² ³")
    print("a |" + ra[0] + "|" + ra[1] + "|" + ra[2] + "|")
    print("   ¹ ² ³")
    print("\n")
    print("")
    played_moves_total += 1

