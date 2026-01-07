
def sorting_meetings(intervals):
    '''
    Selection Sort to sort all the intervals
    
    :param intervals: list of all intervals
    '''
    length = len(intervals) 

    # Selection Sort Algorithm
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if intervals[j][1] < intervals[min_index][1]:
                min_index = j
            
        intervals[i], intervals[min_index] = intervals[min_index], intervals[i]

    return intervals

def min_cancelled_bookings(intervals):
    '''
    Reduces the longest meeting that may take the time of shorter meetings
    
    :param intervals: list of all intervals (meeting times)
    '''
    
    intervals = sorting_meetings(intervals) # Sorting with respect to end time
    count = 0

    last_end = float('-inf')        # Setting to negative of infinity for easy comparision
    for meeting in intervals: 
        if meeting[0] >= last_end:      # If the current meeting has it's start greating than the ending for the last meeting
            last_end = meeting[1]       # We set last end to the last end of the greater start meeting
        else:
            count += 1      # Else we count one meeting to be eliminated
        
    return count

intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]

print("Booking intervals:", intervals)
print("Minimum number of cancellations required:", min_cancelled_bookings(intervals))
