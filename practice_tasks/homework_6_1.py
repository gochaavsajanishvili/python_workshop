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


# print(my_join(lst, '_<3_'))

# Task N_2


# def my_insert(lst, obj, index):
#     temp = lst[index:len(lst) - 1]
#     lst[index] = obj
#     print(temp)
#     for i in temp:
#         lst[index + 1] += i
#     return lst

# print(my_insert(lst, 'lado', 1))


# Task N_5


def my_reverse(lst1):
    reversed_lst = lst1[::-1]
    return reversed_lst


print(my_reverse(lst))
