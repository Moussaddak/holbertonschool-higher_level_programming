#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    list_r = []
    for i in my_list:
        if i % 2 == 0:
            list_r.append(True)
        else:
            list_r.append(False)
    return (list_r)
