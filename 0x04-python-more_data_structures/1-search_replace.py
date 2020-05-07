#!/usr/bin/python3
def search_replace(my_list, search, replace):

    new_list = my_list.copy()
    counter = 0
    for i in my_list:
        if i is search:
            new_list[counter] = replace
        counter += 1
    return (new_list)
