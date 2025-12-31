
# def password_recover(log, pattern):
#     if len(log) < 1:
#         return "Invalid log value"
    
#     if len(pattern) > 10**5:
#         return "Invalid pattern value"
    
#     run = 0
#     detected = ""

#     unique_letter = 0
#     frequency_pattern = {}
#     for key in pattern:
#         if key in frequency_pattern:
#             frequency_pattern[key] += 1
#         else:
#             frequency_pattern[key] = 1
#             unique_letter += 1

#     log_found = {}
#     satisfied = 0
#     shortest = ""
#     length = len(log)
#     repeat = False
    

#     for i in range(len(log)):
#         detected += log[i]

#         if log[i] in pattern:
#             if log[i] in log_found:
#                 log_found[log[i]] += 1
#             else:
#                 log_found[log[i]] = 1

#         if log[i] in log_found:
#             if log_found[log[i]] == frequency_pattern[log[i]]:
#                 satisfied += 1
            
            
#         while satisfied == unique_letter:
            
#             if detected[0] not in pattern or log_found[detected[0]] > frequency_pattern[detected[0]]:
#                 if log_found[detected[0]] > frequency_pattern[detected[0]]:
#                     log_found[detected[0]] -= 1
#                     repeat = True
#                 detected = detected[1:]
                
            
#             elif detected[0] in pattern:
#                 if length >= len(detected):
#                     shortest = detected
#                     length = len(detected)
                
#                 if repeat == True:
#                     detected = detected
#                     log_found = {}
#                 else:
#                     detected = ""
#                     log_found = {}
                
#                 break
    
#     return shortest
    
    
# print(password_recover("ADOBECODEBANC", "BANC"))



print(int(6/2))
print(6//2)