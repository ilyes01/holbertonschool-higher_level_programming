#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        print("{}{}".format(i, j), end="")
        print((", ", "\n")[i == 8 and j == 9], end="")
