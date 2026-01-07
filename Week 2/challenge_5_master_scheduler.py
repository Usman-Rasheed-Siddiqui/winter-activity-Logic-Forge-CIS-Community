
def sorting_meetings(intervals):
    length = len(intervals)

    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if intervals[j][1] < intervals[min_index][1]:
                min_index = j
            
        intervals[i], intervals[min_index] = intervals[min_index], intervals[i]

    return intervals

def min_cancelled_bookings(intervals):
    
    intervals = sorting_meetings(intervals)
    count = 0

    last_end = float('-inf')
    for meeting in intervals:
        if meeting[0] >= last_end:
            last_end = meeting[1]
        else:
            count += 1
        
    return count

print(min_cancelled_bookings([[1, 2], [2, 3], [3, 4], [1, 3]]))