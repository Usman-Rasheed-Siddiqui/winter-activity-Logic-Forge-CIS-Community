
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
    return alerts

def next_alert(alerts):

    NEXT = int(input("Enter Temperature Index for Alert: "))
    print("NEXT", NEXT)

    if alerts[NEXT]:
        return alerts[NEXT]

    else:
        return "No Alert"

def count_alerts(alerts):
    COUNT = int(input("Enter Initial and Final Count Indices with space: ")).split()
    number = 0

    for alert in alerts:
        if alert:
            number += 1
    

    return number

K = 3
temp = [73, 74, 75, 71, 69, 72, 76, 73]

alerts = smart_city_temperature_alert(K, temp)

print(next_alert(alerts))
print(next_alert(alerts))

print(count_alerts(alerts))
print(count_alerts(alerts))

COUNT = []
stop = False

