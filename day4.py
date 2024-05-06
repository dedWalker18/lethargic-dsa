##########################
#    Part 1 for Day 4    #
##########################
## lot of optimisation scope here
## works in O(n^2)

import re

def get_all_numbers(card):
    return re.findall(r"\d+", card)[1:]

def get_matching_numbers(card):
    nums = get_all_numbers(card)
    win_nums = nums[:10]
    own_nums = nums[10:]

    match = 0
    for win_num in win_nums:
        if win_num in own_nums:
            match+=1
            
    return int(match-1)

def get_sum(cards):
    sum = 0
    for card in cards:
        matches = get_matching_numbers(card)
        if matches>=0:
            sum += 2**matches
    return sum

with open('read.txt', "r") as file:
    input = file.read()


## input for testing 

# cards = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
#          "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
#          "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
#          "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
#          "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
#          "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
# ]

cards = input.split("\n")
print(get_sum(cards))