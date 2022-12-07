#!/usr/bin/env python3

import string

alphabet = list(string.ascii_lowercase)
total_priority = 0
total_priority_part_2 = 0

test = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]


def get_priority(value):
    if same_item in alphabet:
        return alphabet.index(same_item) + 1
    else:
        return alphabet.index(same_item.lower()) + 1 + 26


# get all line
with open('day3.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

# part 1
for index, rucksack in enumerate(lines):
    if rucksack.strip():
        # print(repr(rucksack))
        rucksack_size = len(rucksack)
        rucksack_middle = int(rucksack_size/2)
        rucksack_1st = rucksack[:rucksack_middle]
        rucksack_2nd = rucksack[rucksack_middle:]
        # print("Rucksack size: " + str(rucksack_size))
        # print("Comp 1st {} comp 2nd {}".format(rucksack_1st, rucksack_2nd))

        for item in rucksack_1st:
            # print ("item: " + item)
            if item in rucksack_2nd:
                same_item = item
                # print("Same: " + same_item)
                break

        total_priority += get_priority(same_item)

# part 2
for i in range(0, len(lines), 3):
    rucksack = lines[i]
    for item in rucksack:
        if item in lines[i+1] and item in lines[i+2]:
            same_item = item
            break

    total_priority_part_2 += get_priority(same_item)

print("Part 1 - Total Priority: " + str(total_priority))
print("Part 2 - Total Priority: " + str(total_priority_part_2))
