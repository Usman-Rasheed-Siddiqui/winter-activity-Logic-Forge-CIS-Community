
def find_longest_mirror_length(s):
    '''
    Looks for the longest palindrome existing in the string using DP Approach
    
    :param s: string
    '''

    string = s          # String in ascending order
    reverse = s[:: -1]  # String in descending order

    
    len1 = len(string)  
    len2 = len(reverse)

    possibilities = [[0] * (len2 + 1) for _ in range(len1 + 1)]         # Creating a DP for all possibilites

    for i in range(len1):
        for j in range(len2):
            if string[i] == reverse[j]:     # If the first and last matches
                possibilities[i + 1][j + 1] = 1 + possibilities[i][j]       # Add one to the diagonal Possibility
            
            else:
                possibilities[i + 1][j + 1] = max(possibilities[i][j + 1], possibilities[i + 1][j])     # Set diagonal to the maximum of top or left


    return possibilities[len1][len2]        # Return the bottom right (contains the maximum mirror length)


s = "bbabcbcab"

print("Input string:", s)
print("Length of longest palindromic subsequence:", find_longest_mirror_length(s))