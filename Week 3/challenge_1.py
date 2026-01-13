
def smart_city_temperature_alert(K, temp):
    
    alerts = [0 for _ in range(len(temp))]
    j = 1
    i = 0
    while i < j and j < len(temp):
        if temp[j] >= temp[i] + K or temp[j] <= temp[i] - K:
            alerts[i] = j
            i += 1
            j = i + 1
        else:
            j += 1
    
    print(alerts)


K = 3
temp = [73, 74, 75, 71, 69, 72, 76, 73]
smart_city_temperature_alert(K, temp)