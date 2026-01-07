
def sorting_profits(combinations):
    length = len(combinations)

    for i in range(length):
        max_index = i
        for j in range(i + 1, length):
            if combinations[j][1] > combinations[max_index][1]:
                max_index = j
            
        combinations[i], combinations[max_index] = combinations[max_index], combinations[i]

    return combinations

def maximize_freelance_profit(deadlines, profits):

    combinations = []
    for i in range(len(profits)):
        combinations.append((deadlines[i], profits[i]))
    
    combinations = sorting_profits(combinations)
    
    jobs = []
    profits = []

    max_deadline = max(deadlines)
    slots = [0] * (max_deadline + 1)

    for combo in combinations:
        deadline, profit = combo
        for i in range(deadline, 0, -1):
            if slots[i] == 0:
                slots[i] = 1
                jobs.append(combo)
                profits.append(profit)
                break
        

    return [len(jobs), sum(profits)]

deadline = [5, 1, 2, 3, 3, 2]
profits   = [20, 50, 30, 40, 25, 10]

print(maximize_freelance_profit(deadline, profits))