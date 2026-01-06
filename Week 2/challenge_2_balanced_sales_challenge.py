
def can_balance_scales(arr):

    if len(arr) == 0:
        return True

    total = sum(arr)

    split = total // 2

    if split % 2 != 0:
        return False
    
    bagA = {0}
    possibilities = {0}

    for i in range(len(arr)):

        if split in bagA:
            return True
        
        for possibility in bagA:
            possibilities.add(possibility + arr[i])

arr = [10, 20, 30, 40]
print(can_balance_scales(arr))