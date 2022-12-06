#!/usr/bin/env python3

calories_list = []
current_cal_count = 0
num_top = 3

# get all line
with open('day1.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

for entry in lines:
    if entry.strip():
        current_cal_count += int(entry)
    else:
        calories_list.append(current_cal_count)
        current_cal_count = 0

calories_list.sort(reverse=True)
print("Most calories: " + str(calories_list[0]))
top_calories = 0
for i in range(num_top):
    top_calories += calories_list[i]
print("Top {}: {}".format( num_top, str(top_calories)))
