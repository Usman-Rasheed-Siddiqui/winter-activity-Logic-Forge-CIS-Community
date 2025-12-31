
def rise(heap):
    '''
    This function rises the smallest element from an unstable min heap to its right position
    
    :param heap: The heap passed
    '''
    
    index = len(heap) - 1
    parent = (index - 1) // 2

    while parent >= 0:      # Checking until the parent index is valid

        if heap[parent][0] <= heap[index][0]:   # If the parent is already smaller, break
            break
        
        heap[parent], heap[index] = heap[index], heap[parent]   # Else swap the new smallest element
        
        index = parent
        parent = (index - 1) // 2

    return heap

def sink(heap):
    '''
    This function sinks the greatest element from an unstable min heap to its right position
    
    :param heap: The heap passed
    '''

    index = 0

    while True:             # Loop until true
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(heap) and heap[left][0] < heap[smallest][0]:      # If the left child is at wrong position swap it
            smallest = left
        
        if right < len(heap) and heap[right][0] < heap[smallest][0]:    # If the right child is at wrong position swap it
            smallest = right

        if smallest == index:   # If smallest remain unchange break
            break

        else:
            heap[index], heap[smallest] = heap[smallest], heap[index]

    return heap


def deep_storage_inventory_search(matrix, k):
    '''
    Docstring for deep_storage_inventory_search
    
    :param matrix: Matrix to get the correct k
    :param k: The element to be detected
    '''

    length = len(matrix[0])
    heap = []
    i = 0

    for row in matrix:      # Getting initial smallest element from each row
        heap.append((row[0], i, 0))
        i += 1

    for _ in range(k-1):    
        popped = heap[0]
        heap[0] = heap[-1]
        heap.pop(-1)
        heap = sink(heap)   # Replacing the root with child, then deleting it and the getting proper min heap
        
        if popped[2] + 1 < length:      # If the row does not exhausts
            heap.append((matrix[popped[1]][popped[2] + 1], popped[1], popped[2] + 1))   # Add the new smallest element
            heap = rise(heap)   # Rearrange min heap

    return heap.pop(0)[0]   # Return the true element at k position
        
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8

print("Detected Element at k:",deep_storage_inventory_search(matrix, k))