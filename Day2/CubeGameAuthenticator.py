
COLOURS = ["blue", "red", "green"]

with open("Day2/data/games.txt") as f:
    data = f.readlines()

# data = data[20:25]
# print(data)
def build_max_dict(game_events):
    game_handler = {'red': 0, 'green': 0, 'blue': 0}

    pos = 0
    while pos < len(game_events):
        curr_count = int(game_events[pos])
        curr_colour = game_events[pos+1]

        for i in COLOURS:
            if i in curr_colour:
                if curr_count > game_handler[i]:
                    game_handler[i] = curr_count

        pos += 2

    return game_handler

def handle_game(game_text):
    split_text = game_text.split(" ")
    #save game_number without ':'
    game_number = int(split_text[1][:-1])
    # print(game_number)
    game_events = split_text[2:]

    game_dict = build_max_dict(game_events)
    
    return game_dict, game_number
    
def is_good_game(max_dict, game_number):
    if max_dict['red'] > 12 or max_dict['green'] > 13 or max_dict['blue'] > 14:
        print("BAD GAME")
        return 0
    else:
        print("Good Game")
        return game_number

def game1(data):

    game_counter = 0
    for i in data:
        
        max_dict, game_number = handle_game(i)
        game_counter += is_good_game(max_dict, game_number)

    print(game_counter)

def game2(data):
    power_sum = 0
    for i in data:
        max_dict, game_number = handle_game(i)
        power = max_dict['red'] * max_dict['green'] * max_dict['blue']
        power_sum += power

    print(power_sum)

# game1(data)
game2(data)