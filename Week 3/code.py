def smart_city_temperature():
    N, K, Q = 8, 3, 2
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    queries = [
        ("NEXT", 3),
        ("COUNT", 0, 7)
    ]

    INF = 10**9
    next_pos = [INF] * 101
    alerts = [0] * N

    # Precompute alerts
    for i in range(N - 1, -1, -1):
        best = INF

        for t in range(temperatures[i] + K, 101):
            best = min(best, next_pos[t])

        for t in range(30, temperatures[i] - K + 1):
            best = min(best, next_pos[t])

        if best != INF:
            alerts[i] = best

        next_pos[temperatures[i]] = i

    # Prefix sum
    prefix = [0] * N
    prefix[0] = 1 if alerts[0] != 0 else 0
    for i in range(1, N):
        prefix[i] = prefix[i - 1] + (1 if alerts[i] != 0 else 0)

    # Process queries
    for q in queries:
        if q[0] == "NEXT":
            x = q[1]
            print(alerts[x] if alerts[x] != 0 else "No Alert")
        else:
            l, r = q[1], q[2]
            print(prefix[r] - (prefix[l - 1] if l > 0 else 0))


smart_city_temperature()
