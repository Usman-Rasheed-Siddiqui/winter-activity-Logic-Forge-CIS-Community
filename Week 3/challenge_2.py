
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

    print(people)

    people = sorting_people(people)

    l, r = 0, len(people) - 1
    result = 0

    while l <= r:

        if people[l][0] + people[r][0] <= limit and not (people[l][1] == 1 and people[r][1] == 1):
            r -= 1
            l += 1
            result += 1
        else:
            r -= 1
            result += 1 

    return result



inputs = input().split()
N, Q, limit = map(int, inputs)

weight = list(map(int,input().split()))
priority = list(map(int,input().split()))

for _ in range(Q):
    query = input().split()
    if query[0] == "CANPAIR":
        X = query[1]
        Y = query[2]

    elif query[0] == "REMAINING":
        B = query[1]

boats = emergency_evacuation(weight, priority, limit)
print("Minimum boats =", boats)