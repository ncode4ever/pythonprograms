fhand = open('mbox.txt')
count = 0
for l in fhand:
    count = count+1
print ('Line count = ', count)
# Print total numbers of characters
fhand = open('mbox.txt')
print('Total number of characters', len(fhand.read()))

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)