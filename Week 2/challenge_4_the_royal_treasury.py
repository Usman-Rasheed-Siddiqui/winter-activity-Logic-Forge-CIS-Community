

# The recursive approach was difficult and a bit tricky to understand

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
    '''
    Gives all possible ways of reaching the sum with the given coins
    
    :param coins: Array of all coins
    :param total_sum: Sum to approach
    '''

    possibilities = [0] * (total_sum + 1)       # Initializing a DP

    possibilities[0] = 1        # Only one possibility for answer 0

    for coin in coins:          # Looping over coins
        for i in range(coin, total_sum + 1):            # Looping from the current coin to total sum to calculate all the possibilities. This guarantees no coin is revisited backwards
            possibilities[i] += possibilities[i - coin]
    

    return possibilities[total_sum]     # The last index gives the total number of possibilities


coins = [1, 2]
total_sum = 4

print("Coins:", coins)
print("Target sum:", total_sum)
print("Total combinations to reach the sum:", count_payment_combinations(coins, total_sum))
