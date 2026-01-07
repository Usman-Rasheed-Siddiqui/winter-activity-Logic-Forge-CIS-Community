
# def count_payment_combinations(coins, total_sum):

#     possibilities = {}

#     def counting_ways(current, add):
#         if add == total_sum:
#             return 1
        
#         if add > total_sum:
#             return 0
        
#         if current == len(coins):
#             return 0

#         if (current, add) in possibilities:
#             return possibilities[(current, add)]
        
#         possibilities[(current, add)] = counting_ways(current, add + coins[current]) + counting_ways(current + 1, add)
#         return possibilities[(current, add)]
    
#     return counting_ways(0, 0)

# print(count_payment_combinations([1, 2], 4))


def count_payment_combinations(coins, total_sum):

    possibilities = [0] * (total_sum + 1)

    possibilities[0] = 1

    for coin in coins:
        for i in range(coin, total_sum + 1):
            possibilities[i] += possibilities[i - coin]
    

    return possibilities[total_sum]

print(count_payment_combinations([1, 2], 4))
