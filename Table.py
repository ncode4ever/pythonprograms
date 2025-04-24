table = [17, 18, 19, 20]
mul = [1,2,3,4,5,6,7,8,9,10]
fout = open('tables.txt', 'w')  # to write the output file
val = ""
fhand = open('tables.txt')
for i in table:
    print('Table of '+str(i) + ':')
    for j in mul:
        val = val + " " + str(i*j)
    print(val)
    fout.write(val + '\n')  # write to the file
    val = ""
    print('....')
print('Done')
fout.close()

