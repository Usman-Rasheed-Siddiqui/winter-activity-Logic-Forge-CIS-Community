
def rise(heap):
    
    index = len(heap) - 1
    parent = (index - 1) // 2

    while parent >= 0:

        if heap[parent][0] <= heap[index][0]:
            break
        
        heap[parent], heap[index] = heap[index], heap[parent]
        
        index = parent
        parent = (index - 1) // 2

    return heap

def sink(heap):

    index = 0

    while True:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(heap) and heap[left][0] < heap[smallest][0]:
            smallest = left
        
        if right < len(heap) and heap[right][0] < heap[smallest][0]:
            smallest = right

        if smallest == index:
            break

        else:
            heap[index], heap[smallest] = heap[smallest], heap[index]

    return heap


def deep_storage_inventory_search(matrix, k):

    length = len(matrix[0])
    heap = []
    i = 0

    for row in matrix:
        heap.append((row[0], i, 0))
        i += 1

    print(heap)

    for _ in range(k-1):
        popped = heap[0]
        heap[0] = heap[-1]
        heap.pop(-1)
        heap = sink(heap)
        
        if popped[2] + 1 < length:
            heap.append((matrix[popped[1]][popped[2] + 1], popped[1], popped[2] + 1))
            heap = rise(heap)

        print("Heap", heap)

    return heap.pop(0)[0]
        
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8

print(deep_storage_inventory_search(matrix, k))