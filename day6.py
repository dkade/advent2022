#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("Missing signal")
    sys.exit(1)

signal = sys.argv[1]

def get_start(signal, num_char):
    marker = []
    marker_count = 0
    for index, char in enumerate(signal):
        # print("char: {} index: {} marker: {}".format(char, index, marker))
        if char not in marker and marker_count < num_char:
            marker.append(char)
            marker_count +=1
            if marker_count == num_char:
                # print ("start marker" + str(index+1))
                return index+1
        else:
            repeated_char_index = marker.index(char)
            del marker[0:repeated_char_index+1]
            marker.append(char)
            marker_count = len(marker)
            # print("r_c_i: {} count: {} marker: {}".format(repeated_char_index, marker_count, marker))


print("Start of marker: " + str(get_start(signal, 4)))
print("Start of message: " + str(get_start(signal, 14)))
