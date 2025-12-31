
def rise(heap):
    
    index = len(heap) - 1
    parent = (index - 1) // 2

    while parent >= 0:

        if heap[parent] <= heap[index]:
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

        if left < len(heap) and heap[left] < heap[index]:
            smallest = left
        
        if right < len(heap) and heap[right] < heap[index]:
            smallest = right

        if smallest == index:
            break

        else:
            heap[index], heap[smallest] = heap[smallest], heap[index]

    return heap



def deep_storage_inventory_search(matrix, k):
    
    elements = []

    for row in matrix:
        elements.append(row[0])
    
    for _ in range(k):
        heap = rise(elements)
        print("heap:", heap)
        smallest = heap[0]
        print("Smallest:", smallest)
        
        i = 0
        while True:
            if smallest in matrix[i]:
                popping = matrix[i].pop(0)
                print("Popping:", popping)
                if len(matrix[i]) == 0:
                    i += 1

                if matrix[i][0] not in heap:
                    heap[0] = matrix[i][0]
                else:
                    heap[0] = matrix[i][1]

                heap = sink(heap)
                print("Row if smallest:", matrix[i])
                print("Element being placed:", heap[0])
                break
            else:
                i += 1

    return heap[0]

matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8

print(deep_storage_inventory_search(matrix, k))
