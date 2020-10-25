# Homework 6_1

# List For Testing

lst = ['ana', 'gocha', 'ilia', 'mishiko']


# Task N_1


def my_join(lst1, obj):
    join = ''
    index_counter = 0

    for i in lst1:
        index_counter += 1
        if index_counter == len(lst1):
            join += i
            return join
        else:
            join += i + obj
            
            

def my_join(lst1, sep=''):
    # shortest
    join = '' 
    for i in lst1[:-1]:
        join += i + sep
    
    return join + lst1[-1]

def my_join(lst1, sep):
    # with enumerate
    join = ''
    last = len(lst1)
    for index, item in enumerate(lst1, start=1):
        if index == last:
            return join + item

        join += item + sep


# print(my_join(lst, '_<3_'))

# Task N_2


def my_insert(lst1, obj, index):
    first_half = lst1[0:index]
    second_half = lst1[index:len(lst1)]

    first_half += [obj]
    new_lst = first_half + second_half

    print(new_lst)
    
def my_insert(lst1, obj, index):
    return lst1[:index] + [obj] + lst1[index:]


# my_insert(lst, 'lado', 2)


# Task N_3
# With del method


def my_pop(lst1, index=-1):
    last_obj = lst1[index]
    del lst1[index]
    return last_obj

# Without del method


def my_pop_no_del(lst1, index=-1):
    first_half = lst1[0:index]
    if index >= 0:
        second_half = lst1[index+1:len(lst1)]
        new_lst = first_half + second_half
        lst1 = new_lst
    else:
        return first_half
    return lst1


def my_pop_no_del(lst1, index=-1):
    first_half = lst1[:index]
    second_half = lst1[index+1:]    
    print(first_half + second_half)
    return lst1[index]
# With del test
# print(my_pop(lst))
# print(lst)

# Without del test
# lst = my_pop_no_del(lst, 3)
# print(lst)

# Task N_4


def my_remove(lst1, obj):
    counter = 0
    new_lst = []
    for i in lst1:
        if lst1[counter] == obj:
            new_lst = my_pop_no_del(lst1, counter)
        else:
            counter += 1
    return new_lst


# lst = my_remove(lst, 'mishiko')
# print(lst)


# Task N_5


def my_reverse(lst1):
    reversed_lst = lst1[::-1]
    return reversed_lst


# print(my_reverse(lst))

# Task N_6


def my_sort(lst1):
    n = len(lst1)

    for i in range(n):
        for j in range(n - i - 1):
            if lst1[j] > lst1[j + 1]:
                lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]

    print(lst1)


my_sort(lst)
