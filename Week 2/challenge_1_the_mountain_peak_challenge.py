
import time

def count_ways_to_summit(n):
    '''
    The count ways to summit actually follows the Fibonacci Sequence to count the number of possible ways.
    Hence a simple Fibonacci series code can solve the problem.
    
    :param n: Total number of steps to reach the top
    '''

    prev = 0            # Passed sum
    current = 0         # Current number

    for _ in range(1, n + 1):   # Looping over to get the required sequence

        temp = prev         # Temporary variable to save previous
        prev = current      # Previous set to current

        if prev == 0:       # Checking case if prev gets 0
            current += 1
            prev = 1
        else:
            current += temp     # Current gets add up with the previous digit

    return current      

start = time.time()
print("Number of ways of climbing mountain:",count_ways_to_summit(45))
end = time.time()
print(f"Time: {end - start} sec")