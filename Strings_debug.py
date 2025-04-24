new_line = ''
while True:
    line = input('>')
    if line[0] == '#':
        new_line = new_line + line
        continue
    if line == 'done':
        break # after this break next 1 line will not be executed
    print(line)
print(new_line)
print('Done !!!')    
    