#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    max = my_list[0]
    for i in range(1, len(my_list)):
        if max < my_list[i]:
            max = my_list[i]
        else:
            continue
    return (max)
