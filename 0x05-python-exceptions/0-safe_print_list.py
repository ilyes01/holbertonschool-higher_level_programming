#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb = 0
    for nb in range(x):
        try:
            print(end="{}".format(my_list[nb]))
            nb += 1
        except IndexError:
            break
    print()
    return nb
