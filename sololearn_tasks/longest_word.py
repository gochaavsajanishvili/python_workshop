txt = input()
words = txt.split(',')
better_words = []
counter = []

for i in words:
    better_words += i.split()

for i in better_words:
    counter.append(len(i))

for i in better_words:
    if max(counter) == len(i):
        print(i)
