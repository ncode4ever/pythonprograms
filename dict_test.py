count = {'chuck':1, 'larry':2, 'King':3, 'Ellison':4}
print(count.get('King',0))

word = 'SachinTendulkar'
d = dict()
i = 0
for c in word:
    d[c] = d.get(c,0) + i
    i = i+1
print(d)
print(d['a'])