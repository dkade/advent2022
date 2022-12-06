#!/usr/bin/env python3


# Rock Paper Scissors
# 1 2 3
# A B C
# X Y Z

DRAW_VALUE = 3
WIN_VALUE = 6

game = {
    '1': ['A', 'X'], # rock
    '2': ['B', 'Y'], # paper
    '3': ['C', 'Z']  # scissors
}

victory_cond = {
    '2':'1',
    '3':'2',
    '1':'3'
}

def get_hand_value(hand):
    for k, v in game.items():
        if hand in v:
            return k

def get_winning_hand_score(opp, me):
    opp = get_hand_value(opp)
    me = get_hand_value(me)
    if opp == me:
        return int(me) + DRAW_VALUE
    my_choice = victory_cond[me]
    if opp in my_choice: # I win
        return int(me) + WIN_VALUE
    else:
        return int(me)

def get_rigged_result(opp, result):
    opp = get_hand_value(opp)
    if result == 'Y':
        return int(opp) + DRAW_VALUE
    if result == 'X':
        return int(victory_cond[opp])
    else:
        my_choice = dict((new_val,new_k) for new_k,new_val in victory_cond.items()).get(opp)
        return int(my_choice) + WIN_VALUE

    
def current_play(values):
    opp = values[0]
    me = values[2]
    return (get_winning_hand_score(opp, me), get_rigged_result(opp, me))

# get all line
with open('day2.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

my_score = 0
new_score = 0
for entry in lines:
    if entry.strip():
        part1, part2 = current_play(entry)
        my_score += part1
        new_score += part2

# part 1
print("part 1: " + str(my_score))

# part 2
print("part 1: " + str(new_score))
