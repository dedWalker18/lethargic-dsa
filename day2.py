####################
# Part 1 for Day 2 #
####################

## uses some more regex
## lot of optimisation scope here
## works in O(nk)

## input used for testing
## input = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
##          "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
##         "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
##         "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
##         "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
##         ]

import re

def check_possibility(color_counts):
    if color_counts['green'] <= 13 and color_counts["red"] <= 12 and color_counts["blue"] <= 14:
        return True
    return False
  
def get_color_counts(game_string):
    matches = re.findall(r"(\d+)\s+([a-z]+)", game_string)
    color_counts = {}
    for count, color in matches:
        count = int(count)
        color_counts[color] = max(color_counts.get(color, 0), count)
    return color_counts

def check_games(games): 
    for game in games:
        if game == "":
            break
            
        all_nums = re.findall(r'\d+',game)
        flag = (True for num in all_nums if int(num) > 15)
        if not flag:
            continue
            
        color_counts = get_color_counts(game)
        if check_possibility(color_counts):
            game = re.findall(r'Game\s\d+', game)
            id.append(int(re.findall(r'\d+', game[0])[0]))
            
id = []

with open('read.txt', "r") as file:
    input = file.read()

games = input.split("\n")
check_games(games)
print(sum(id))