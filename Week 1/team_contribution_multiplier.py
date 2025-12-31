
def contrib_multipler(contributions):
    '''
    This code calculates contributions of each element of the array. It has two separate loops
    Making O(n) + O(n) = O(n) Time Complexity
    Excluding the output array i.e. impact[] the Space Complexity is O(1).
    '''
    
    impact = [1]    

    left = 1
    # last index is never counted when traversing for left side impact
    for i in range(1, len(contributions)):
        left = left * contributions[i-1]    # Left impact calculation
        impact.append(left)     # Appending to the impact list

    right = 1
    # The last loop muliplies the right side impacts with their respective left side impacts
    for i in range(len(contributions)-1, -1, -1):
        impact[i] = right * impact[i]   # Multiply left impacts by right impacts
        right = right * contributions[i]    # Calculate new right impact for next element

    return impact

print(contrib_multipler([1, 2, 3, 4]))
