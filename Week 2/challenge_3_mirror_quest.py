
def find_longest_mirror_length(s):

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

print(find_longest_mirror_length("bbabcbcab"))