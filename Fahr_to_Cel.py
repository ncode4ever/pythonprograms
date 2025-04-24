f = input('Enter Temperature in F')

try:
    c = (int(f) -32 ) * 5/9
    print('Temperature is ' + str(round(c,2)))
except:
    print('Enter Valid Number')