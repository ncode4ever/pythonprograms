counts = dict()
line = input('Enter a Line : ')
words = line.split()

print('Words : ', words)
print('Counting....')

for i in words:
    counts[i] = counts.get(i, 0) + 1
print('Counts', counts)
