
def smart_city_temperature(N, K, Q):

    temperatures = list(map(int, input().split()))
    if len(temperatures) != N:
        print("Invalid number of inputs")
        return

    # next_warmer = [0]*N 
    alerts = [0]*N 
    stack = []
    for i, temp in enumerate(temperatures):
        while stack and ((temperatures[i] >= stack[-1][0] + K) or (temperatures[i] <= stack[-1][0] - K)):
            stackt, idx = stack.pop()
            alerts[idx] = i
        stack.append([temp, i])
    
    # next_colder = [0]*N  
    # stack = []
    # for i in range(N):
    #     while stack and (temperatures[i] <= temperatures[stack[-1]] - K):
    #         idx = stack.pop()
    #         next_colder[idx] = i
    #     stack.append(i)

    
    # for i in range(N):
    #     if next_warmer[i] != 0 and next_colder[i] != 0:
    #         alerts[i] = min(next_warmer[i], next_colder[i])

    #     elif next_warmer[i] != 0:
    #         alerts[i] = next_warmer[i]

    #     elif next_colder[i] != 0:
    #         alerts[i] = next_colder[i]

    # print(alerts)

    for _ in range(Q):
        operation = input().split()

        if operation[0] == "NEXT":
            X = int(operation[1])
            print(alerts[X] if alerts[X] != 0 else "No Alert")
        
        elif operation[0] == "COUNT":
            L = int(operation[1])
            R = int(operation[2])
            count = 0
            for a in range(L,R+1):
                if alerts[a] != 0:
                    count += 1
            
            print(count)
        

inputs = list(map(int, input().split()))
N, K, Q = inputs[0], inputs[1], inputs[2]

smart_city_temperature(N, K, Q)