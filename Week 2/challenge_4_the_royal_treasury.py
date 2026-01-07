
def count_payment_combinations(coins, total_sum):

    sums = []

    count = 0
    for i in range(total_sum):
        if count <= total_sum:
            sums.append(count)
            count += 1

    add = 0
    possibilities = []
    while add != total_sum:
            add += coins[i]



    for i in range(len(coins)):
        while add != total_sum:
            coins[i] += add



        
