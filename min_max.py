num_list = [11,13,15,16,89,123,56,78,23]
min = None
max = None
for i in num_list:
    if min is None or min > i:
        min = i
    if max is None or max < i:
        max = i
print('Min = '+str(min))
print('Max = '+str(max))