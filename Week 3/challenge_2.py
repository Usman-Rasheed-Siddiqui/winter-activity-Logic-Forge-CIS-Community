
def sorting_people(people):
    '''
    Selection Sort to sort all the people
    
    :param people: list of all people
    '''
    length = len(people) 

    # Selection Sort Algorithm
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if people[j][0] < people[min_index][0]:
                min_index = j
            
        people[i], people[min_index] = people[min_index], people[i]

    return people

def emergency_evacuation(weight, priority, limit):

    people = []
    for i in range(len(weight)):
        people.append((weight[i], priority[i]))

    people = sorting_people(people)

    l, r = 0, len(people) - 1
    result = 0

    while l <= r:

        if people[l][0] + people[r][0] <= limit and not (people[l][1] == 1 and people[r][1] == 1):
            r -= 1
            l += 1
        else:
            r -= 1
        result += 1 

    return result, people

def canpair(x, y, weight, priority):
    if weight[x] + weight[y] <= limit and not (priority[x] == 1 and priority[y] == 1):
        return "Yes"
    else:
        return "No"
    
def remaining(B, people, limit):
    people = sorted(people, key=lambda x: x[0])
    l, r = 0, len(people) - 1
    boats = []
    evacuated = 0
    boats_used = 0

    while l <= r:

        if l < r and people[l][0] + people[r][0] <= limit and not (people[l][1] == 1 and people[r][1] == 1):
            boats.append(2)
            r -= 1
            l += 1

        else:
            r -= 1
            boats.append(1)
        boats_used += 1

    boats_sorted = sorted(boats, reverse=True)
    max_people_evacuated = sum(boats_sorted[:B])
        
    return len(people) - max_people_evacuated


inputs = input().split()
N, Q, limit = map(int, inputs)

weight = list(map(int,input().split()))
priority = list(map(int,input().split()))

boats, sorted_people = emergency_evacuation(weight, priority, limit)
print("Minimum boats =", boats)

for _ in range(Q):
    query = input().split()
    if query[0] == "CANPAIR":
        X = int(query[1])
        Y = int(query[2])
        print(canpair(X, Y, weight, priority))

    elif query[0] == "REMAINING":
        B = int(query[1])
        print(remaining(B, sorted_people, limit))