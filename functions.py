def greet_function(first_name, last_name):
    print(f"Welcome {first_name} {last_name} !!")
    print("Welcome to the Python world")


def get_greet_function():
    return greet_function("KNOW", "LEDGE")


greet_function("John", "Doe")
print(get_greet_function())
