
def scrambled_keyword_search(s, p):
    """
    Find all starting indices in s where an anagram of p occurs.

    :param s: string to search in
    :param p: pattern string (anagram)
    :return: list of starting indices
    """

    word_dict = {}
    search_dict = {}
    for word in p:  # Count letters in pattern
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            search_dict[word] = 0   # Count letters in first window of s

    result = []
    # Slide the window
    for i in range(len(s)):
        if s[i] in word_dict:   # Add new character
            search_dict[s[i]] += 1

        if i >= len(p):     
            left_indx = i - len(p)
            left_most = s[left_indx]
            if left_most in search_dict:
                search_dict[left_most] -= 1
        # Compare window with pattern
        if i >= len(p) - 1:
            if search_dict == word_dict:
                result.append(i - len(p) + 1)

    return result

string = "cbaebabacd"
window = "abc"

print("String:", string)
print("Pattern:", window)
print("Pattern found at:", scrambled_keyword_search(string, window))