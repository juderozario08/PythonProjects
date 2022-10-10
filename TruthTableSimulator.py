# This program creates a truth table for a logical statement given by the user. 
# After getting the input from the user, create a truth table for each individual variable,
# Then for each individual term separated by '+' and then the entire logical statement
# The program can also check for logical equivalence if the user chooses to do so.
# At first the program will ask whether the user just wants the truth table or 
# do they want to check for logical equivalence between 2 statements.
# Write all the output to a file called output.txt

# NOTE : THE PROGRAM ONLY WORKS WITH SIMPLIFIED LOGICAL STATEMENTS

# The format for input is:
# '+' means OR
# Eg. a+b
# If two or more logical variables are written together without any symbols, it represents AND
# Eg. ab
# For the negation of a logical variable, we use "'" apostrophe.
# Eg. a'
# No bracket operations are included in this program
# Example of a proper logical statement: ab' + bc' + cd


# Open a file and call it output.txt
file = open("output.txt","w")
def truthTableSim(logic):
    # Empty list to store base inputs
    inputs = [] 
    # Go through the for loop and append every input in the logic to the inputs list
    for i in logic: 
        if i != "'" and i!= "`" and i != '+' and i.isalpha():
            if i not in inputs: 
                inputs.append(i)
    inputs = sorted(inputs)
    # Invidual terms from the statement
    terms = logic.replace(" ", "").split("+") 
    # Counter for alternating bool values
    counter = 1 
    # Dictionary for storing bools for base values
    boolInputs = {} 
    # Dictionary for storing bools for specific terms separated by spaces
    termBools = {} 
    # Dictionary for storing the bool value of the final term
    logicBools = {} 
    
    # Append the complementary inputs in the inputs as well for the final bool values
    for i in range(len(inputs)):
        inputs.append(inputs[i]+"'")
    # The base number of inputs without the complementary set
    realNumOfInputs = int(len(inputs)/2)
    
    # Create a truth table for every input based on the number of inputs given.
    # Take those bool values and store them inside a dictionary. 
    # The key being the input and the output being the list of bool values
    for i in range(realNumOfInputs):
        counter = 1  
        boolInputs[inputs[i]] = regularTruthTable(counter,i+1,realNumOfInputs)
    
    # Add the bool values of the complementary inputs in the boolInputs dictionary
    for i in range(realNumOfInputs, len(inputs)): 
        boolInputs[inputs[i]] = [False if j else True for j in boolInputs[inputs[i][0]]]
        
    # In the termBools dictionary input the term as the key and truth table as the value
    for term in terms:
        termBools[term] = termTruthTable(term,boolInputs,realNumOfInputs)
    # Write in file all inputs and it's complements and their bool values
    file.write("Base Inputs\n")
    for i in range(len(inputs)):
        if len(inputs[i]) == 1: file.write(f"{inputs[i]} : {boolInputs[inputs[i]]}\n")
        else: file.write(f"{inputs[i]}: {boolInputs[inputs[i]]}\n")
            
    # Get rid of all spaces from the logical statement to avoid errors
    logic = logic.replace(" ", "")
    # Get the bool values for the main logical statement
    logicBools[logic] = mainLogicBool(terms, termBools, realNumOfInputs)
    # Write in file all the terms and their truth table separately
    file.write("\nLogical Terms\n")
    for term in terms:
        file.write(f"{term} : {termBools[term]}\n")
    # Write in file the logical statement and its Boolean Values Separately
    file.write("\nLogical Statement\n")
    file.write(f"{logic} : {logicBools[logic]}\n\n")
    return logicBools[logic]

# Based on the index being looked at, the values in a truth table changes after every 2^(n-index+1)
# Using that input the bool values in the empty list 
# Update the value of counuter accordingly
# Return the mapped truth table for the given input
def regularTruthTable(counter,index,realNumOfInputs):
    tempBoolList = [] # Empty list
    tempBool = False # Default bool value
    for i in range(2**realNumOfInputs):
        # Alternate the bool values based on the index of the input and append it to the list
        if counter > 2**(realNumOfInputs-index):
            counter = 1
            if tempBool: tempBool = False
            else: tempBool = True 
        tempBoolList.append(tempBool)
        counter += 1
    return tempBoolList

# Get the truth table for every term separately
def termTruthTable(term, boolInputs, realNumOfInputs):
    termTable = [] # Empty truth table for the terms
    termInputs = [] # The types of input in the term
    for i in range(len(term)):
        # Check whether the input is a complement or not
        # Then use the values from the boolInputs dictionary to figure out the final bool value of the term
        if term[i:i+2] == term[i] + "'" or term[i:i+2] == term[i] + "`":
            termInputs.append(term[i] + "'")
            i+=1
        elif term[i].isalpha():
            termInputs.append(term[i])
    # Default bool value for the term
    termBool = False
    # If all there is a single input that is false, break out of loop and change bool of the term to false
    # Else make the boolean value True and then append it to the truth table for the term
    for i in range(2**realNumOfInputs):
        for j in termInputs:
            if not boolInputs[j][i]:
                termBool = False
                break
            else: termBool = True
        termTable.append(termBool)
    # Return the truth table of the term
    return termTable

# Gets the truth table for the logical statement
def mainLogicBool(terms, termBools, realNumOfInputs):
    # Empty bool table for the main logic
    logicTable = [] 
    # Default bool value
    tempBool = False
    # Loop through the truth values of all the terms
    # If there is a single term that returns true, break the loop and append True to the logic table
    for i in range(2**realNumOfInputs):
        for j in terms:
            # j is the term i is the bool value for the term
            if termBools[j][i]: 
                tempBool = True
                break
            else: tempBool = False
        logicTable.append(tempBool)
    # Return the truth table of the logical statement
    return logicTable

# Checks if two different logical statements are equal.
# If the truth values of both logics are equal, then that means they are logically equivalent.
# 
def logicalEquivalence(statementA, statementB):
    boolValuesA = truthTableSim(statementA)
    boolValuesB = truthTableSim(statementB)
    file.write(f"{statementA} and {statementB} are logically equivalent.\n" 
          if boolValuesA == boolValuesB else "Not logically equivalent\n")
            
        
if __name__ == "__main__":
    # Create a bool value for if the equation is valid
    validEqn = False
    # Common symbols
    symbols = "'+` "
    # Check whether the user wants logical equivalence or a regular truth table simulator
    logicalEqv = False
    # Checks whether the users choice for the operation they want to do is valid
    validAnswer = False
    # Empty string for storing user inputs
    chooseFunc = ""
    logic = ""
    statementA = ""
    statementB = ""
    while not validAnswer:
        chooseFunc = input("Type one of the options\nLogical Equivalence Calculator or Truth Table Simulator: \n")
        chooseFunc = chooseFunc.strip()
        if chooseFunc == "Logical Equivalence Calculator" or chooseFunc == "Truth Table Simulator": 
            logicalEqv = True
            break
    if logicalEqv: 
        # Loop forever until 
        while not validEqn:
            # Get the logical statement from the user and until its valid, continue asking for the logic
            statementA = input("Enter a valid logic: ")
            # For every character in the statement, if the statament contains that are not valid, make validEqn false
            for i in statementA: 
                if i not in symbols and not i.isalpha():
                    validEqn = False # Make sure the equation is invalid
                    break
                else: validEqn = True # Make sure the equation is valid if there are no logical errors
        validEqn = False
        # Loop forever until 
        while not validEqn:
            # Get the logical statement from the user and until its valid, continue asking for the logic
            statementB = input("Enter a valid logic: ")
            # For every character in the statement, if the statament contains that are not valid, make validEqn false
            for i in statementB: 
                if i not in symbols and not i.isalpha():
                    validEqn = False # Make sure the equation is invalid
                    break
                else: validEqn = True # Make sure the equation is valid if there are no logical errors
        validEqn = False
        logicalEquivalence(statementA, statementB)
    else:
        while not validEqn:
            # Get the logical statement from the user and until its valid, continue asking for the logic
            logic = input("Enter a valid logic: ")
            # For every character in the statement, if the statament contains that are not valid, make validEqn false
            for i in logic: 
                if i not in symbols and not i.isalpha():
                    validEqn = False # Make sure the equation is invalid
                    break
                else: validEqn = True # Make sure the equation is valid if there are no logical errors
        truthTableSim(logic)