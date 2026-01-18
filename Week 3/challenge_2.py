
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
    """
    Calculate minimum number of boats needed to evacuate all people
    given weight limits and priority restrictions.
    
    :param weight: list of weights
    :param priority: list of priorities (1 = high, 0 = normal)
    :param limit: weight limit per boat
    :return: (min boats, sorted people by weight)
    """

    # Combine weight and priority for each person
    people = []
    for i in range(len(weight)):
        people.append((weight[i], priority[i]))

    # Sort people by weight
    people = sorting_people(people)

    l, r = 0, len(people) - 1
    result = 0

     # Loop until all people are evacuated
    while l <= r:
        # Can we pair the lightest and heaviest?
        if people[l][0] + people[r][0] <= limit and not (people[l][1] == 1 and people[r][1] == 1):
            r -= 1
            l += 1
        else:   # Otherwise, heaviest person goes alone
            r -= 1
        result += 1 

    return result, people

def canpair(x, y, weight, priority):
    """
    Check if two people can share a boat.
    
    :param x: index of first person
    :param y: index of second person
    :param weight: list of weights
    :param priority: list of priorities
    :return: "Yes" or "No"
    """
    # Condition: total weight <= limit and both are not priority 1
    if weight[x] + weight[y] <= limit and not (priority[x] == 1 and priority[y] == 1):
        return "Yes"
    else:
        return "No"
    
def remaining(B, people, limit):
    """
    Calculate number of people who cannot be evacuated using B boats.

    :param B: number of boats available
    :param people: sorted list of (weight, priority)
    :param limit: weight limit per boat
    :return: number of people left behind
    """
    # Sort people by weight to use two-pointer pairing
    people = sorted(people, key=lambda x: x[0])
    l, r = 0, len(people) - 1
    boats = []
    evacuated = 0
    boats_used = 0

    # Greedy pairing: lightest + heaviest if possible
    while l <= r:
        if l < r and people[l][0] + people[r][0] <= limit and not (people[l][1] == 1 and people[r][1] == 1):
            boats.append(2)
            r -= 1
            l += 1

        else:
            r -= 1
            boats.append(1)
        boats_used += 1
    # Each boat can carry max 2 people
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