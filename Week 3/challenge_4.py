
def scrambled_keyword_search(s, p):

    word_dict = {}
    search_dict = {}
    for word in p:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            search_dict[word] = 0

    result = []
    for i in range(len(s)):
        if s[i] in word_dict:
            search_dict[s[i]] += 1

        if i >= len(p):
            left_indx = i - len(p)
            if search_dict == word_dict:
                result.append(left_indx)

            left_most = s[left_indx]
            if left_most in search_dict:
                search_dict[left_most] -= 1
            
    return result

print(scrambled_keyword_search("cbaebabacd", "abc"))


        
