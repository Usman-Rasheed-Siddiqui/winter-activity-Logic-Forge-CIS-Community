
def sorting_profits(combinations):
    '''
    Implementing selection sort in descending order
    
    :param combinations: All the deadline and profit combo
    '''
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
    for i in range(len(profits)):       # Making pairs
        combinations.append((deadlines[i], profits[i]))
    
    combinations = sorting_profits(combinations)
    
    jobs = []
    profits = []

    max_deadline = max(deadlines)       # Getting the maximum deadline
    slots = [0] * (max_deadline + 1)        # Creating empty slots for job

    for combo in combinations:         
        deadline, profit = combo
        for i in range(deadline, 0, -1):         # Looping to check for empty slots
            if slots[i] == 0:               # If slot is empty set it to 1 and append that job to jobs and add the profit to profits
                slots[i] = 1
                jobs.append(combo)
                profits.append(profit)
                break
        
    return [len(jobs), sum(profits)]

deadline = [5, 1, 2, 3, 3, 2]
profits   = [20, 50, 30, 40, 25, 10]

print("Deadlines:", deadline)
print("Profits:", profits)
result = maximize_freelance_profit(deadline, profits)
print("Maximum jobs:", result[0])
print("Maximum profit:", result[1])