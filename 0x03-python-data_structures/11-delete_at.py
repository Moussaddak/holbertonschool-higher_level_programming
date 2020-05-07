#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    if idx > len(my_list) or idx < 0:
        return (my_list)
    for i in my_list:
        if my_list.index(i) is idx:
            del my_list[i]
    return (my_list)
