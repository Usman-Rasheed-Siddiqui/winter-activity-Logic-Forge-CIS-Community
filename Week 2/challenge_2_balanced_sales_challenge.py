
def can_balance_scales(arr):
    '''
    This code gives True if the weight of the stones can be divided equally into to bags.
    
    :param arr: Array containing weights of the individual stones.
    '''

    # Base case
    if len(arr) == 0:
        return True

    total = sum(arr)    # The total weight

    if total % 2 != 0:  # If we do not get an even weight (odd can't be separated)
        return False
    
    split = total // 2  # Dividing weight to half
    
    possibilities_bagA = [0]          # Initializing a list of possibilities of weight in bagA (using only one bag. If this is balanced the next one will be auto balanced)
    possibilities = {0} # The possibilites of weight that can occur in bagA

    for i in range(len(arr)):   

        if split in possibilities_bagA:   # If the divided weight is present 
            return True
        
        for possibility in possibilities_bagA:      # Looping over possibilites in A bag and adding them to the new possibility
            possibilities.add(possibility + arr[i])

        possibilities_bagA = list(possibilities)

    return split in possibilities

arr = [1, 3, 5]
print("Array:", arr)
print("Can be balanced:", can_balance_scales(arr))