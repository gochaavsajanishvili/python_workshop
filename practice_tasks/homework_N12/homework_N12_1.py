if __name__ == '__main__':
    with open('file_N1.txt') as file:
        names = file.readlines()
        names.sort(key=lambda marks: int(marks.split()[-1]))
        with open('file_N2.txt', 'w') as file2:
            for name in names:
                file2.write(name)
