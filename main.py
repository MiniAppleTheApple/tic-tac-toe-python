SIZE = 3

def calculate_position(x, y):
    return x + y * 3

def next_round(round):
    if round == "x":
        return "o"
    else:
        return "x"

def text_format_table(table):
    text = ""
    for x, v in enumerate(table):
        if x % SIZE == 0 and x != 0:
            text += "|\n"
        
        text += f"|{v}"

    text += "|"

    return text

def is_any_player_winned_by_row(table, round):
    for x in range(SIZE):
        count = 0
        for y in range(SIZE):
            if table[calculate_position(x, y)] == round:
               count += 1
        if count == 3:
            return True
    return False

def is_any_player_winned_by_column(table, round):
    for y in range(SIZE):
        count = 0
        for x in range(SIZE):
            if table[calculate_position(x, y)] == round:
               count += 1
        if count == 3:
            return True
    return False

def is_any_player_winned_by_slope(table, round):
    count = 0 
    for pos in range(SIZE):
        if table[calculate_position(pos, pos)] == round:
               count += 1

    if count == SIZE:
        return True

    count = 0

    for pos in range(SIZE):
        if table[calculate_position(SIZE - 1 - pos, SIZE - 1 - pos)] == round:
               count += 1

    if count == SIZE:
        return True


def is_any_player_winned(table, round):
    return is_any_player_winned_by_row(table, round) or is_any_player_winned_by_column(table, round) or is_any_player_winned_by_slope(table, round)

def is_filled(table):
    return all(map(lambda x: x != " ", table))

INITIAL_TABLE = [
    "x", "o", "x",
    "x", "o", "o",
    "o", "x", " ",
]

STARTING_PLAYER = "x"

if __name__ == "__main__":
    # Clone the list
    table = INITIAL_TABLE[:]

    round = STARTING_PLAYER

    is_game_done = False

    while not is_game_done:
        print(text_format_table(table)) 

        x = int(input("x axis: "))
        y = int(input("y axis: "))

        position = calculate_position(x, y)

        if table[position] == " ":
            table[position] = round
        else:
            print("This block is occupied")
            continue

        print(is_any_player_winned(table, round))

        if is_any_player_winned(table, round):
            print(f"{round} winned")
            break

        if is_filled(table):
            print("Reseting the game")
            # Reset
            round = STARTING_PLAYER
            table = INITIAL_TABLE
            continue 

        round = next_round(round)
