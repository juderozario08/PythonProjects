# Within the function:
# Iterate over the list contents using some kind of loop. If the integer at that position is not equal to 4, set the va># multiplied by your input scalar.
# However, if your list item at any index is equal to 4, then don't multiply it by the scalar and keep it as it is!
# After you have looped through the whole list and multiplied the scalar throughout (accounting for special 4 behaviour>

# Outside of the function (in the if __name__ == "__main__" block):
# First create an empty list.
# Then, set some integer num_ints to user input, representing the amount of integers that should be added to the list.
# Prompt the user to enter an integer num_ints times, and for each integer they enter add it to the list.
# Then, prompt the user to enter some scalar value that will be multiplied into the list.
# Finally, print the call of the above function using the (now non-empty) list and the integer as inputs.

def operation(ls, scalar):
    # If length of set list and the length of original list does not match, that means there were duplicates in the original list and hence we can return -1.
    if len(set(ls)) != len(ls):  # Bonus
        return -1
    # Iterate through the users list and check if the number is 4
    # If it is not, then multiply the scalar to it
    # Else just add the number in the list
    for i in range(len(ls)):
        if ls[i] != 4:
            ls[i] *= scalar
    # Return the updated list
    return ls


if __name__ == "__main__":
    # Create an empty list
    ls = []
    # Get input from the user for how many numbers they want
    size = int(input("How many numbers? "))
    # Go through a for loop and add the user inputs for the numbers in the list
    for i in range(size):
        ls.append(int(input("Number: ")))
    # Get the scalar input from the user
    scalar = int(input("Enter Scalar Value: "))
    # Print the final updated list using another function by passing in the user created list and the scalar
    print(operation(ls, scalar))
