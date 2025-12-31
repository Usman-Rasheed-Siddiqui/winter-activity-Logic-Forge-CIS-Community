def countWrongParanthesis(string):
    left, right = 0, 0

    for char in string:
        if char == "(":
            left += 1

        elif char == ")":
            if left > 0:
                left -= 1
            
            else:
                right += 1

    return left, right

def combinationCheck(string, left, right, start, pairs):
    if isValid(string):
        pairs.append(string)

    for i in range(len(string)):
        if i > start and string[i] == string[i - 1]:    # To avoid duplicates
            continue

        parenthes = string[i]

        if left > 0 and parenthes == "(":
            combinationCheck(string[:i] + string[i + 1:], left - 1, right, i, pairs)

        if right > 0 and parenthes == ")":
            combinationCheck(string[:i] + string[i + 1:], left, right - 1, i, pairs)

def isValid(string):
    left, right = countWrongParanthesis(string)
    if left == 0 and right == 0:
        return True
    return False

def fix_broker_expression(string):

    if not 1 <= len(string) <= 25:
        return "Expression limit exceeded"
    
    parenthesis = 0
    for char in string:
        if char in "()":
            parenthesis += 1

    if parenthesis > 20:
        return "Parenthesis limit exceeded"
        
    left, right = countWrongParanthesis(string)
    pairs = []

    combinationCheck(string, left, right, 0, pairs)

    return pairs


string = "()())()"

print(fix_broker_expression(string))
