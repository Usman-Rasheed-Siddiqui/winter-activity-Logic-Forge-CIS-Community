
def smart_city_temperature_alert(N, K, Q):
    
    temperatures = (input(f"Enter {N} days' temperatures with spaces: ")).split()
    temperatures = [int(i) for i in temperatures]

    alerts = [0 for _ in range(len(temperatures))]
    j = 1
    i = 0
    while i < j and j < len(temperatures):
        if temperatures[j] >= temperatures[i] + K or temperatures[j] <= temperatures[i] - K:
            alerts[i] = j
            i += 1
            j = i + 1
        else:
            j += 1
    
    print(alerts)

    next_query_num = Q // 2
    counr_query_num = Q // 2
    next_query = []
    count_query = []


    for i in range(next_query_num):

        NEXT = 0
        NEXT = int(input("NEXT "))
        if alerts[NEXT]:
            next_query.append(alerts[NEXT])
        else:
            next_query.append("No Alert")

    for i in range(counr_query_num):
        COUNT = input("COUNT ").split()
        COUNT = [int(i) for i in COUNT]
        number = 0
        for i in range(COUNT[0], COUNT[1] + 1):
            if alerts[i]:
                number += 1

        count_query.append(number)

    for i in range(Q//2):
        print(next_query[i])

    for i in range(Q//2):
        print(count_query[i])




inputs = input("").split()
inputs = [int(i) for i in inputs]
N, K, Q = inputs[0], inputs[1], inputs[2]

alerts = smart_city_temperature_alert(N, K, Q)

