
def balanced_performance(scoreA, scoreB):

    lengthA = len(scoreA)
    lengthB = len(scoreB)
    total_length = lengthA + lengthB
    median_index = int(total_length / 2)


    median = 0
    previous = None
    current = None
    seen = 0
    ptrA = 0
    ptrB = 0

    while seen <= median_index:

        previous = current

        if ptrA < lengthA and ptrB < lengthB:

            if scoreA[ptrA] < scoreB[ptrB]:
                current = scoreA[ptrA]
                ptrA += 1
                seen += 1
            else:
                current = scoreB[ptrB]
                ptrB += 1
                seen += 1

        elif ptrA >= lengthA:
            current = scoreB[ptrB]
            ptrB += 1
            seen += 1

        elif ptrB >= lengthB:
            current = scoreA[ptrA]
            ptrA += 1
            seen += 1

    if total_length % 2 == 0:
        median = (previous + current) / 2
    else:
        median = float(current)

    return median
    
print(balanced_performance([1, 2, 3], [4]))            
