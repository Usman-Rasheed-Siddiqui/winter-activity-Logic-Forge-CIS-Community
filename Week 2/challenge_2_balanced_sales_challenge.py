
def can_balance_scales(arr):

    if len(arr) == 0:
        return True

    total = sum(arr)

    split = total / 2

    if split % 2 != 0:
        return False

    arr.sort()
    bagA = arr
    bagB = []

    for i in range(len(arr)):
        if bagB:
            if sum(bagA) == sum(bagB) == int(split):
                return True
        temp = bagA.pop(0)
        bagB.append(temp)
    
    return False

arr = [10, 20, 30, 40]
print(can_balance_scales(arr))