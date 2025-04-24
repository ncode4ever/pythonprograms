import time
initime = time.time()
fhand = open('mbox.txt')
fout = open('mails.txt', 'w')  # to write the output file
count = 0
word_count = 0

for l in fhand:
    l = l.strip()
    # Count words in this line by splitting on whitespace and counting non-empty elements
    words = [word for word in l.split() if word]
    word_count += len(words)
    if l.startswith('From:'):
        email_line = l.strip('From: ')
        print(email_line + '\n')  # prints the line containing From
        fout.write(email_line + '\n')  # write to the file
        count = count + 1
    else:
        continue
fout.close()  # close opened file mails.txt
fhand.close()  # close opened file mbox.txt
print('Total number of lines:', count)
print('Total number of words:', word_count)
print('Total time to execute:', time.time() - initime)