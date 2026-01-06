

def palindrome_check(string):
    
    i = 0
    j = len(string)
    palindrome = True

    while i < j:
        if string[i] != string[j]:
            palindrome = False
            break
        
        i += 1
        j -= 1

    return palindrome


def find_longest_mirror_length(s):

    length = len(s)

    if length == 1:
        return 1
    
    temp = s

    for i in range(length):
        if temp[0] != temp[length - 1]:
            if palindrome_check(temp[1:]):
                return len(temp[1:])
            
            elif palindrome_check(temp[:length - 1]):
                return len(temp[1:])

find_longest_mirror_length("abcb")
