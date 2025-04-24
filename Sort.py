def sort_letters(input_string):
    # Remove spaces and convert string to a list of characters
    input_string = input_string.replace(" ", "")
    
    # Sort the letters alphabetically
    sorted_string = ''.join(sorted(input_string))
    
    return sorted_string

# Example usage:
input_string = input("Enter a string of letters: ")
sorted_string = sort_letters(input_string)
print("Sorted string:", sorted_string)
