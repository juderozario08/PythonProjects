# Write a Python program that will take one input from the user made up of two strings separated by a comma and a space (see samples below). Then create a mixed string with alternative characters from each string. Any leftover chars will be appended at the end of the resulting string. [ Do not use lists for this task]
def alternatingString(string):
    return ''.join([string[0:string.find(", ")][i:i+1]+string[string.find(", ") + 2:len(string)][i:i+1]
                    for i in range(max(len(string[0:string.find(", ")]), len(string[string.find(", ") + 2:len(string)])))])


print(alternatingString("ABCD, efgh") == "AeBfCgDh" and alternatingString("ABCDENDFGH, ijkl")
      == "AiBjCkDlENDFGH" and alternatingString("ijkl, ABCDENDFGH") == "iAjBkClDENDFGH")
