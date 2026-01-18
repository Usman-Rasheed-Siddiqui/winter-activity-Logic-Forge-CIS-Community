

def longest_mirrored_phrase(s):
    
    s1 = s
    s2 = s[::-1]

    n = len(s1)
    m = len(s2)
    
    dp = [[0] * (m + 1) for i in range (n + 1)]
    
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] += 1 + dp[i][j]

            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    
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


print(longest_mirrored_phrase("BBABCBCAB"))

