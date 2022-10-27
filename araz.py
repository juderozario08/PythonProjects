# Write a Python program that will take one input from the user made up of two strings separated by a comma and a space (see samples below). Then create a mixed string with alternative characters from each string. Any leftover chars will be appended at the end of the resulting string. [ Do not use lists for this task]
def alternatingString(string):
    # Find the index of ", " from the string
    index = string.find(", ")
    # Make the letters to the left of the , as string 1
    # And make the letters to the right of the , as string 2
    string1 = string[0:index]
    string2 = string[index+2:len(string)]
    # Initialize the result string which will store the inputs
    result = ''
    smallStringSize = min(len(string1), len(string2))
    # Add all the characters alternating between the indexes of both strings
    for i in range(smallStringSize):
        result += string1[i]+string2[i]
    # If both strings are equal, then we can return the result as the for loop would be enough to finish the condition
    if len(string1) == len(string2):
        return result
    # Add the rest of the larger string to the result using string indexing
    elif len(string1) > len(string2):
        result += string1[smallStringSize:len(string1)]
        return result
    else:
        result += string2[smallStringSize:len(string2)]
        return result


print(alternatingString("ABCD, efgh") == "AeBfCgDh" and alternatingString("ABCDENDFGH, ijkl")
      == "AiBjCkDlENDFGH" and alternatingString("ijkl, ABCDENDFGH") == "iAjBkClDENDFGH")
