
def hours_check(low, high, mid, piles):
    
    piles = piles[low : high + 1]
    result = piles[mid]
    
    count = 0
    for i in range(len(piles)):
        count += (piles[i] + piles[mid] - 1) // piles[mid]
    
    if count == result:
        return True
    
    return False

def calculate_minimum_speed(piles, k):

    low = 0
    high = len(piles) - 1

    while low < high:
        mid = (low + high) // 2
        result = hours_check(low, high, mid, piles)

        if result:
            return mid
        
        elif result <= k:
            high = mid
        
        else:
            low = mid + 1

    return mid
