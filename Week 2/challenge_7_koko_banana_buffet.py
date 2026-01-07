 
def hours_check(piles, mid):
    
    count = 0
    for pile in piles:
        count += (pile + mid - 1) // mid

    return count



def calculate_minimum_speed(piles, k):

    low = 1
    high = max(piles)

    while low < high:
        
        mid = (low + high) // 2
        result = hours_check(piles, mid)
        if mid == result:
            return mid
        
        elif mid <= k:
            high = mid

        else:
            low = mid - 1

    return mid
