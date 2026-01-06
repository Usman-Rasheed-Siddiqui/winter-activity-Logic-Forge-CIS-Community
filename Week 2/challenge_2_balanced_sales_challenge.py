
def can_balance_scales(arr):

    if len(arr) == 0:
        return True

    total = sum(arr)

    if total % 2 != 0:
        return False
    
    split = total // 2
    
    bagA = [0]
    possibilities = {0}

    for i in range(len(arr)):

        if split in bagA:
            return True
        
        for possibility in bagA:
            possibilities.add(possibility + arr[i])

        bagA = list(possibilities)

    return split in possibilities

arr = [2, 4, 6, 1]
print(can_balance_scales(arr))