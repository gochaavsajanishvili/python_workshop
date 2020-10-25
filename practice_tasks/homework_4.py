# Homework 4

# Globally declared functions


def spaces(num):
    print(' ' * num, end='')


def sequence(up_to):
    for i in range(1, up_to):
        print(i, end='')


# Task A


def h_repeated(n):
    print('#' * n, end='')


def hash_triangles():
    for i in range(1, 9):
        spaces(9 - i)
        h_repeated(i)
        print(' ', end='')
        h_repeated(i)
        print()

    print()

    for i in range(1, 9):
        spaces(i)
        h_repeated(9 - i)
        print(' ', end='')
        h_repeated(9 - i)
        print()


# Task B


def numbered_sequence(up_to):
    for i in range(0, up_to):
        print(i, end='')


def number_triangle():
    for i in range(0, 10):
        numbered_sequence(i + 1)
        print()


# Task C


def reversed_sequence(down_to):
    for i in range(down_to, 0, -1):
        print(i, end='')


def numbered_pyramid():
    for i in range(1, 10):
        spaces(9 - i)
        sequence(i + 1)
        reversed_sequence(i - 1)
        print()


# Task D


def reverse_sequence(down_to):
    for i in range(down_to, 0, -1):
        print(i, end='')


def number_pyramid():
    for i in range(1, 10):
        spaces(9 - i)
        sequence(i)
        reverse_sequence(i)
        print()


def inverted_pyramid():
    for i in range(1, 9):
        spaces(i)
        sequence(9 - i)
        reverse_sequence(9 - i)
        print()


if __name__ == '__main__':
    # Main
    print('Task A')
    hash_triangles()
    print('Task B')
    number_triangle()
    print()
    print('C')
    numbered_pyramid()
    print()
    print('Task D')
    number_pyramid()
    inverted_pyramid()
