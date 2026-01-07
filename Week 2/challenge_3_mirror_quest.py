
def find_longest_mirror_length(s):

    string = s
    reverse = s[:: -1]

    
    len1 = len(string)
    len2 = len(reverse)

    possibilities = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1):
        for j in range(len2):
            if string[i] == reverse[j]:
                possibilities[i + 1][j + 1] = 1 + possibilities[i][j]
            
            else:
                possibilities[i + 1][j + 1] = max(possibilities[i][j + 1], possibilities[i + 1][j])


    return possibilities[len1][len2]

s = "bbabcbcab"
print(find_longest_mirror_length(s))