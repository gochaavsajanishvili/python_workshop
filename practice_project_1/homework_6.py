# Homework 6

# List For Testing

lst1 = ['ana', 'gocha', 'ilia', 'mishiko']

# Task N1


def my_append(lst, obj):
    lst += [obj]

# my_append(lst, 'lavrenti')

# Task N2


def my_count(lst, obj):
    count = 0
    for i in lst:
        if i == obj:
            count += 1
    return count

# print(my_count(lst, 'gocha'))

# Task N3


def my_index(lst, obj):
    index = 0
    for i in lst:
        if(i == obj):
            return index
        else:
            index += 1


# print(my_index(lst, 'ilia'))

if __name__ == '__main__':
    print(my_index(lst1, 'ilia'))
