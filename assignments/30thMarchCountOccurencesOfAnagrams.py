# Count Occurences of Anagrams
# Raman is a keen observer, he can easily see the jumbled words so one day one of his friend challenged him to count the occurrences of all the anagrams of string C in a given string S. Raman accepted the challenge but he is facing some problems in it . Can you help them ?

# Input:

# S=fororfrdofr  
# C=for   
# Output: 3

# Input :

#  S=aabaabaa  
#  C=aaba  
# Output: 4

# 1<=s.length, c.length<=10^3

from collections import Counter

def count_occurrences_of_anagrams(S, C):
    len_s, len_c = len(S), len(C)
    
    if len_c > len_s:
        return 0
    
    count_c = Counter(C)
    window = Counter(S[:len_c])
    count = 0
    
    if window == count_c:
        count += 1
    
    for i in range(len_c, len_s):
        start_char = S[i - len_c]
        new_char = S[i]
        
        # Add new character to the window
        window[new_char] += 1
        
        # Remove the start character from the window
        window[start_char] -= 1
        if window[start_char] == 0:
            del window[start_char]
        
        # Compare window with count_c
        if window == count_c:
            count += 1
            
    return count

# Test cases
print(count_occurrences_of_anagrams("fororfrdofr", "for"))  # Output: 3
print(count_occurrences_of_anagrams("aabaabaa", "aaba"))    # Output: 4
