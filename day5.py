#!/usr/bin/env python3

# will use lists instead of a queue for fun

test = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

input = [['R', 'S', 'L', 'F', 'Q'], ['N', 'Z', 'Q', 'G', 'P', 'T'], ['S', 'M', 'Q', 'B'], ['T', 'G', 'Z', 'J', 'H', 'C', 'B', 'Q'], ['P', 'H', 'M', 'B',
                                                                                                                                     'N', 'F', 'S'], ['P', 'C', 'Q', 'N', 'S', 'L', 'V', 'G'], ['W', 'C', 'F'], ['Q', 'H', 'G', 'Z', 'W', 'V', 'P', 'M'], ['G', 'Z', 'D', 'L', 'C', 'N', 'R']]

instructions = ["move 1 from 2 to 1", "move 3 from 1 to 3",
                "move 2 from 2 to 1", "move 1 from 1 to 2"]


def parse_instruction(inst):
    instruction_dict = {}
    instruction_dict["number_of_crates"] = int(inst.split(" ")[1])
    instruction_dict["origin_stack"] = int(inst.split(" ")[3])
    instruction_dict["target_stack"] = int(inst.split(" ")[5])
    return instruction_dict


with open('day5.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

# instructions = instructions
# ship = test
instructions = lines
ship = input

# part 1
# for instruction in instructions:
#     instruction = parse_instruction(instruction)
#     print(str(instruction))
#     for x in range(0, instruction["number_of_crates"]):
#         crate = ship[instruction["origin_stack"]-1].pop()
#         print("Crate: " + crate)
#         ship[instruction["target_stack"]-1].append(crate)

# part 2
print(str(ship))
for instruction in instructions:
    instruction = parse_instruction(instruction)
    # print(str(instruction))
    crates = ship[instruction["origin_stack"] -
                  1][-instruction["number_of_crates"]:]
    ship[instruction["origin_stack"]-1] = ship[instruction["origin_stack"] -
                                               1][:-instruction["number_of_crates"]]
    # print("Crates: " + str(crates))
    ship[instruction["target_stack"]-1].extend(crates)
    # print(str(ship))


top_crates = []
for index, containers in enumerate(ship):
    # print("{} - {}".format(index+1, containers))
    top_crates.append(containers[-1])

# print(str(top_crates))
print(''.join(top_crates))
