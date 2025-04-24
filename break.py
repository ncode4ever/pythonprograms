sucessful = False
for number in range(4):
    print("Attempt ", number + 1)
    if number == 2:
        sucessful = True
    if sucessful:
        print("Successful")
        break
    else:
        print("Unsuccessful")
        continue
print("Done with attempts")
