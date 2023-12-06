#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if my_list and len(my_list):
        nbr = 0
        d = 0
        for tup in my_list:
            nbr += (tup[0] * tup[1])
            d += tup[1]
        return (nbr / d)
    return 0
