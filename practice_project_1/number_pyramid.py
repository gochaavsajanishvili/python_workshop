# Homework 4

# Spaces Declared globally for all tasks


def spaces(num):
    print(' ' * num, end='')

# Task A


def upper_triangles(up_to):
    for i in range(1, up_to + 1):
        print('#', end='')


def lower_triangles(down_to):
    for i in range(down_to, 0, -1):
        print('#', end='')


def hash_triangles():
    for i in range(1, 9):
        spaces(9 - i)
        upper_triangles(i)
        print(' ', end='')
        upper_triangles(i)
        print()
    print()

    for i in range(1, 9):
        spaces(i)
        lower_triangles(9 - i)
        print(' ', end='')
        lower_triangles(9 - i)
        print()


# Task D


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
    # Main
    hash_triangles()
    print()
    number_pyramid()
    inverted_pyramid()
