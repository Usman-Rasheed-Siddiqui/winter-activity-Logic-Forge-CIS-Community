
def countWrongParanthesis(string):
    '''
    This function counts the number of redundant parenthesis either left or right.
    
    :param string: String of parenthesis and characters
    '''
    left, right = 0, 0

    for char in string:
        if char == "(":     # If left bracket exist increment left
            left += 1

        elif char == ")":    # If right bracket exist check if there is a left bracket, if yes decrease left, if not increase right
            if left > 0:
                left -= 1
            
            else:
                right += 1

    return left, right

def combinationCheck(string, left, right, start, pairs):
    '''
    Docstring for combinationCheck
    
    :param string: String of parenthesis and characters
    :param left: left redundant parenthesis
    :param right: right redundant parenthesis
    :param start: index to start checking from
    :param pairs: list of correct pairs
    '''
    
    if isValid(string):     # If the detected pattern is valid
        pairs.append(string)

    for i in range(start, len(string)):        # Looping on the given string
        if i > start and string[i] == string[i - 1]:    # To avoid duplicates
            continue

        parenthes = string[i]

        if left > 0 and parenthes == "(":   # If left redundant brackets are present, remove that parenthes and check that string
            combinationCheck(string[:i] + string[i + 1:], left - 1, right, i, pairs)

        if right > 0 and parenthes == ")":  # If right redundant brackets are present, remove that parenthes and check that string
            combinationCheck(string[:i] + string[i + 1:], left, right - 1, i, pairs)

def isValid(string):
    '''
    This function checks if there are no redundant left and right parenthesis.
    
    :param string: String of parenthesis and characters
    '''
    left, right = countWrongParanthesis(string) # Calling function to get the left and right redundant parenthesis
    if left == 0 and right == 0:
        return True
    return False

def fix_broker_expression(string):
    '''
    This is the main function that calls all the functions and calculates all possible valid combinations
    
    :param string: String of parenthesis and characters
    '''

    if not 1 <= len(string) <= 25:      # Constraint
        return "Expression limit exceeded"
    
    parenthesis = 0
    for char in string:
        if char in "()":
            parenthesis += 1

    if parenthesis > 20:    # Constraint
        return "Parenthesis limit exceeded"
        
    left, right = countWrongParanthesis(string)
    pairs = []

    combinationCheck(string, left, right, 0, pairs)

    return pairs

string = "((("

print("Broken Expression:", string)
print("Fixes:",fix_broker_expression(string))
