# Homework 4
# Task D


def spaces(num):
    print(' ' * num, end='')


def sequence(up_to):
    for i in range(1, up_to + 1):
        print(i, end='')


def reverse_sequence(down_to):
    for i in range(down_to, 0, -1):
        print(i, end='')


def number_pyramid():
    for i in range(1, 10):
        spaces(9 - i)
        sequence(i)
        reverse_sequence(i - 1)
        print()


def inverted_pyramid():
    for i in range(1, 9):
        spaces(i)
        sequence(9 - i)
        reverse_sequence(8 - i)
        print()


if __name__ == '__main__':
    number_pyramid()
    inverted_pyramid()
