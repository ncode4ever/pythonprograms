# creating a function to check whether the list item is a positive
# or a negative number
def positive_or_negative():
    # accepting user input and converting it to a list of integers
    user_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in user_input.split()]
    # traversing in the user-provided list
    for i in numbers:
        if i == 0:
            print(str(i) + " is Zero")
        elif i < 0:
            print(str(i) + " is Negative number")
            break
        if i >= 0:
            print(str(i) + " is Positive number")
        else:
            print(str(i) + " is Negative number")
            break
    else:
        print("Loop-else Executed")


# Calling the above-created function
positive_or_negative()
