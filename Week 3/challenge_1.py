
def smart_city_temperature(N, K, Q):

    temperatures = list(map(int, input().split()))
    if len(temperatures) != N:
        print("Invalid number of inputs")
        return
    
    alerts = [0 for i in range(len(temperatures))]
    j = 1
    i = 0
    while j > i and j != len(temperatures):
        if temperatures[j] >= temperatures[i] + K or temperatures[j] <= temperatures[i] - K:
            alerts[i] = j
        i += 1
        j = i + 1
    
    for i in range(Q):
        operation = input().split()

        if operation[0] == "NEXT":
            X = int(operation[1])
            print(alerts[X] if alerts[X] != 0 else "No Alert")
        
        elif operation[0] == "COUNT":
            L = int(operation[1])
            R = int(operation[2])
            count = 0
            for i in range(L,R+1):
                if alerts[i]:
                    count += 1
            
            print(count)
        

inputs = list(map(int, input().split()))
N, K, Q = inputs[0], inputs[1], inputs[2]

smart_city_temperature(N, K, Q)