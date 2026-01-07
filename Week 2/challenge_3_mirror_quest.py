
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


def find_longest_mirror_length(s, index):

    length = len(s)
    longest_length = 0

    # odd length

    for i in range(length):
        left, right = i, i
        while left <= 0 and right < length and s[left] == s[right]:
            temp_length = (right - left) + 1
            if temp_length > longest_length:
                longest_length = temp_length
            
            left -= 1
            right += 1

    for  i in range(length):
        left = i
        right = i + 1
        while left <= 0 and right < length and s[left] == s[right]:
            temp_length = (right - left) + 1
            if temp_length > longest_length:
                longest_length = temp_length
            
            left -= 1
            right += 1
    
    return longest_length