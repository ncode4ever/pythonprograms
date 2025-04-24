val = input("Enter a number: ")
val = int(val)
if val > 50:
    print("Value is greater than 50")
elif val == 50:
    print("Value is equal to 50")
else:
    print("Value is less than 50")
print("Done !!!")

message = "Greater than 50" if val > 50 else "Equal" if val == 50 else "Less than or equal to 50"
print(message)
