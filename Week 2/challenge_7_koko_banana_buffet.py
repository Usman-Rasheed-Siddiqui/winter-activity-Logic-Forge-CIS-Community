 
def hours_check(piles, mid):
    '''
    Calculate the number of houts the piles will take with the given speed
    
    :param piles: The piles of banana
    :param mid: Binary search mid
    '''
    
    count = 0
    for pile in piles:      # Calculating ceiling of each pile by the mid and adding it to count the number of hours the piles will take
        count += (pile + mid - 1) // mid

    return count

def calculate_minimum_speed(piles, k):
    '''
    Calculate the minimum Speed in which the piles can be finished
    
    :param piles: The piles of banana
    :param k: The total number of hours to finish the piles
    '''

    low = 1         # Min time
    high = max(piles)   # Max time

    while low < high:
        
        mid = (low + high) // 2
        result = hours_check(piles, mid)
        
        if result <= k:     # If the result is smaller or equal to the given hours, increase speed
            high = mid

        else:
            low = mid + 1   # Else move slower

    return low  # Return the slowest speed possible


piles = [5, 10, 15, 20]
k = 7

print("Banana piles:", piles)
print("Hours available:", k)
print("Minimum eating speed to finish in time:", calculate_minimum_speed(piles, k), "bananas/hour")