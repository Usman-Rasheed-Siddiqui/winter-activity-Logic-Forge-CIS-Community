

def longest_mirrored_phrase(s):
    """
    Find the longest mirrored phrase (longest palindromic subsequence) in a string.

    :param s: input string
    :return: longest mirrored phrase as string
    """
    
    s1 = s
    s2 = s[::-1]    # reversed string

    n = len(s1)
    m = len(s2)
    # DP table for LCS
    dp = [[0] * (m + 1) for i in range (n + 1)]
    
    # Fill DP table
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] += 1 + dp[i][j]     # add match

            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])    # take max of left/up
    # Reconstruct the palindrome from DP table
    i, j = n, m
    palindrome = ""
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            palindrome += s1[i - 1]
            i -= 1
            j -= 1
        
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return palindrome


string = "babad"
print("String:", string)
print("Longest Palindrome Subsequence:",longest_mirrored_phrase(string))

