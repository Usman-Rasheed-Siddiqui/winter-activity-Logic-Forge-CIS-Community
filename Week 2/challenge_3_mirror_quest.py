
def find_longest_mirror_length(s):

    length = len(s)

    if length == 1:
        return 1

    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            max_string = max(s[i + 1:], s[i: j])
            return find_longest_mirror_length(max_string)
        
        else:
            return 2 + find_longest_mirror_length(s[i + 1: ])

print(find_longest_mirror_length("bbabcbcab"))
