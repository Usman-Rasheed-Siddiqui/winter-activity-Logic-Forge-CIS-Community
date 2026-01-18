
def smart_city_temperature(N, K, Q):
    """
    Compute earliest alert days for temperatures and answer queries.

    :param N: Number of days
    :param K: Threshold difference for alerts
    :param Q: Number of queries
    """

    # Read the list of temperatures
    temperatures = list(map(int, input().split()))
    if len(temperatures) != N:
        print("Invalid number of inputs") # Safety check
        return

    # Initialize alert days for each index to 0 (no alert)
    alerts = [0]*N 
    # Using a stack to try to find next alert days
    stack = []
    for i, temp in enumerate(temperatures):
        # Pop from stack while current temperature is >= K warmer or <= K colder than top of stack
        while stack and ((temperatures[i] >= stack[-1][0] + K) or (temperatures[i] <= stack[-1][0] - K)):
            stackt, idx = stack.pop()
            alerts[idx] = i
        stack.append([temp, i])
    
    # Process queries
    for _ in range(Q):
        operation = input().split()

        # NEXT Operations
        if operation[0] == "NEXT":
            X = int(operation[1])
            print(alerts[X] if alerts[X] != 0 else "No Alert")  # Output alert day or "No Alert"
        
        # COUNT operation
        elif operation[0] == "COUNT":
            L = int(operation[1])
            R = int(operation[2])
            count = 0

            # Count number of non-zero alerts in range [L,R]
            for a in range(L,R+1):
                if alerts[a] != 0:
                    count += 1
            
            print(count)
        

inputs = list(map(int, input().split()))
N, K, Q = inputs[0], inputs[1], inputs[2]

smart_city_temperature(N, K, Q)

# I tried a lot of times to match count 4 for given example test case but it fails. To match
# But this code covers all other examples correctly given by GPT