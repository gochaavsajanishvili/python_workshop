def hanoi(n, start: str, end: str):
    middle = 'ABC'.strip(start+end)
    if n == 3:
        print(
            f'''
            {start} -> {middle}
            {start} -> {end}
            {middle} -> {end}
            {start} -> {middle}
            {end} -> {middle}
            {end} -> {start}
            {middle} -> {start}
            {start} -> {end}
            {start} -> {middle}
            {start} -> {end}
            {middle} -> {end}
            '''
        )
        return None

    hanoi(n-1, start, middle)
    print(' '*11, f'{start} -> {end}')
    hanoi(n-1, middle, end)


hanoi(3, 'A', 'C')
