#!/usr/bin/env python3

test = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8"
]

with open('day4.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

pair_count = 0
part_count_part_2 = 0

# part 1
for index, sections in enumerate(lines):
    if sections.strip():
        elf_a_section = sections.split(',')[0]
        elf_b_section = sections.split(',')[1]
        elf_a_start = int(elf_a_section.split('-')[0])
        elf_a_end = int(elf_a_section.split('-')[1])
        elf_b_start = int(elf_b_section.split('-')[0])
        elf_b_end = int(elf_b_section.split('-')[1])
        print(elf_a_section)
        if elf_a_start <= elf_b_start and elf_a_end >= elf_b_end:  # a<=c b>=d
            pair_count += 1
            part_count_part_2 += 1
            continue  # because 3-3,3-3 will match on both IFs
        if elf_a_start >= elf_b_start and elf_a_end <= elf_b_end:
            pair_count += 1
            part_count_part_2 += 1
            continue
        if (elf_b_start <= elf_a_start <= elf_b_end) or (elf_b_start <= elf_a_end <= elf_b_end):
            part_count_part_2 += 1


print("Part 1 - Pair Count: " + str(pair_count))
print("Part 2 - Pair Count: " + str(part_count_part_2))
