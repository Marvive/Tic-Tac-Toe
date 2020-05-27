barrier = "---------"
entry = "_________"
# entry = input("Enter cells:")
# entry = "X_X_O____"

entry_dict = {
    "1 3": entry[0],
    "2 3": entry[1],
    "3 3": entry[2],
    "1 2": entry[3],
    "2 2": entry[4],
    "3 2": entry[5],
    "1 1": entry[6],
    "2 1": entry[7],
    "3 1": entry[8],
}

winning_options = [
    ["1 3", "2 3", "3 3"],
    ["1 2", "2 2", "3 2"],
    ["1 1", "2 1", "3 1"],
    ["1 3", "1 2", "1 1"],
    ["2 3", "2 2", "2 1"],
    ["3 3", "3 2", "3 1"],
    ["1 3", "2 2", "3 1"],
    ["1 1", "2 2", "3 3"],
]


def print_board():
    print(f"""{barrier}
| {entry_dict['1 3']} {entry_dict['2 3']} {entry_dict['3 3']} |  
| {entry_dict['1 2']} {entry_dict['2 2']} {entry_dict['3 2']} |
| {entry_dict['1 1']} {entry_dict['2 1']} {entry_dict['3 1']} |
{barrier}""")


result = ""


def check_winner():
    global result
    for options in winning_options:
        # if all(elem == options[0] for elem in options):
        if entry_dict[options[0]] == entry_dict[options[1]] and entry_dict[options[1]] == entry_dict[options[2]]:

            result = f"{entry_dict[options[0]]} wins"
            break
    if not any(value == "_" for value in entry_dict.values()):
        if "X" in result or "O" in result:
            pass
        else:
            result = "Draw"


# GAME
print_board()
turn_counter = 0
while result != "X wins" and result != "O wins" and result != "Draw":
    next_input = input("Enter the coordinates:")
    next_move = next_input.split()
    if len(next_move) != 2:
        print("There must be two integers separated by a space.")
        continue
    else:
        try:
            x_input = int(next_move[0])
            y_input = int(next_move[1])
        except ValueError:
            print("You should enter numbers!")
            continue

    if x_input not in range(1, 4) or y_input not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        continue

    # if place is taken on board, continue
    if entry_dict[next_input] is "_":
        if turn_counter % 2 == 0:
            entry_dict[next_input] = "X"
        else:
            entry_dict[next_input] = "O"
        print_board()
        turn_counter += 1
        check_winner()
        if result[0] != "_":
            print(result)
    else:
        print("This cell is occupied! Choose another one!")
        continue



