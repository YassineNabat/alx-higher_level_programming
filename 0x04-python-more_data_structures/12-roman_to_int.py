#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    dic = [roman_dict[x] for x in roman_string]
    index = 0
    for i in range(len(decs)):
        index += dic[i]
    return index
