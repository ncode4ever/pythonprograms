def mutiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(mutiply(2, 3, 4, 5))
