
def scrambled_keyword_search(s):
    
    l, r = 0, len(s) - 1

    palindrome_left = ""
    palindrome_right = ""
    while l <= r:
        left_char = s[l]
        right_char = s[r]
        if left_char == right_char:
            palindrome_left += left_char
            palindrome_right += right_char

            l += 1
            r -=



