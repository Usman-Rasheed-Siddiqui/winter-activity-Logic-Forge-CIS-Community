
def can_balance_scales(arr):

    if len(arr) == 0:
        return True

    arr.sort()
    bagA = arr
    bagB = []

    for i in range(len(arr)):
        if bagB:
            if sum(bagA) == sum(bagB):
                return True
        temp = bagA.pop(0)
        bagB.append(temp)
    
    return False

arr = [10, 20, 30, 40]
print(can_balance_scales(arr))