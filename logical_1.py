age = input("Enter your age: ")
age = int(age)
# if statement
if age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are not an adult.")
# simpler way of if statement
if 18 <= age < 65:
    print("You are an adult !!!.")
else:
    print("You are not an adult !!.")
print("Done with age check.")
