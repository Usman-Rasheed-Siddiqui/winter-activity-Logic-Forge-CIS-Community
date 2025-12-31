
def password_recover(log, pattern):
    '''
    Docstring for password_recover
    
    :param log: The string in which the password's pattern is hidden
    :param pattern: The original pattern to be recovered from the string
    '''
    if len(log) < 1:                # Constraint
        return "Invalid log value"
    
    if len(pattern) > 10**5:        # Constraint
        return "Invalid pattern value"
    
    pattern_found = {}
    log_found = {}
    need = 0

    for key in pattern:             # Original Pattern's Unique Character Count
        if key in pattern_found:
            pattern_found[key] += 1
        else:
            pattern_found[key] = 1
            log_found[key] = 0
            need += 1
            
    satisfied = 0
    length = len(log)
    shortest = None
    
    start = 0
    end = 0
    
    for i in range(len(log)):       # Loop on the whole string
        
        if log[i] in pattern_found: # If the current character is present in the pattern
            log_found[log[i]] += 1
            
            if log_found[log[i]] == pattern_found[log[i]]:      # If the log dict's character's values matches pattern dict's character's values
                satisfied += 1
            
        while satisfied == need:        # When the needed characters are satisfied in the already detected log pattern
            end = i
            temp = (end - start) + 1
            if temp < length:           # If the current pattern has the smaller length then that of the previous detected
                length = temp
                shortest = (start, end)

            if log[start] in log_found:     # If the detected smallest pattern's first index is a pattern character, decrease it's value in the log dict
                log_found[log[start]] -= 1  # This allows for more pattern detection if they also have the pattern character
            
            if log[start] in pattern_found and log_found[log[start]] < pattern_found[log[start]]:   # This allows for more pattern detection if they also have the pattern character
                satisfied -= 1

            start += 1      # This increments the start arbitrarily to start checking a sequence for pattern

    if shortest is not None:        # Checking if the pattern is detected, else return an empty string
        start, end = shortest
        return log[start: end + 1]
    else:
        return ""
                     
print(password_recover("ADOBECODEBANC", "ABC"))