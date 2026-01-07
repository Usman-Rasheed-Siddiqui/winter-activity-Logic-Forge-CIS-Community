
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

    for combo in combinations:
        if combo[0] > len(jobs):
            jobs.append(combo[0])
            profits.append(combo[1])
            
    return [len(jobs), sum(profits)]



print(maximize_freelance_profit([2, 1, 2, 1, 1], [100, 19, 27, 25, 15]))