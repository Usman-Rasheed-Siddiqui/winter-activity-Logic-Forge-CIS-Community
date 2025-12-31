
def balanced_performance(scoreA, scoreB):
    '''
    This function allows for calculating median without merging the two input arrays.
    
    :param scoreA: Scores of A team in ascending order
    :param scoreB: Scores of B team in ascending order
    '''

    lengthA = len(scoreA)
    lengthB = len(scoreB)
    total_length = lengthA + lengthB
    median_index = int(total_length / 2)

    if not 0 <= lengthA <= 1000 and not 0 <= lengthB <= 1000:
        return "Scores limit breached"

    if not 1 <= total_length <= 2000:
        return "Total scores limit breached"

    median = 0
    previous = None
    current = None
    seen = 0
    ptrA = 0
    ptrB = 0

    while seen <= median_index: # If the seen characters count is equal to where a median can be detected

        previous = current      # At every loop we set the previous one to the current of the last loop

        if ptrA < lengthA and ptrB < lengthB:   # Checking if the pointer running is less than the original length of the list

            if scoreA[ptrA] < scoreB[ptrB]:     # If A's score is less than B's score
                current = scoreA[ptrA]
                ptrA += 1
                seen += 1
            else:
                current = scoreB[ptrB]
                ptrB += 1
                seen += 1

        elif ptrA >= lengthA:       # If the pointer of A has exceeded the length of A
            current = scoreB[ptrB]
            ptrB += 1
            seen += 1

        elif ptrB >= lengthB:       # If the pointer of B has exceeded the length of B
            current = scoreA[ptrA]
            ptrA += 1
            seen += 1

    if total_length % 2 == 0:       # If the number of scores of given lists adds up to an even number.
        median = (previous + current) / 2
    else:                           # If the number of scores add up to odd number
        median = float(current)

    return median
    
scoreA = [1, 2]
scoreB = [3, 4]

print("Team A Score:", scoreA)
print("Team B score", scoreB)
print("Median of all the scores:",balanced_performance(scoreA, scoreB))            
