from collections import Counter

def permutation_in_String_Optimized(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_count = Counter(s1)
    
    left = 0
    window_count = Counter()
    window_size = len(s1)
    
    for right in range(len(s2)):
        window_count[s2[right]] +=1

        # Window size to compare
        if right - left + 1 > window_size:
            left_char = s2[left]
            window_count[left_char] -= 1
            
            # if the size is big remove the element to maintain the size
            if window_count[left_char] == 0:
                del window_count[left_char]

            left += 1
        
        if window_count == s1_count:
            return True
        
    return False

s1 = "adc"
s2 = "dcda"
print(permutation_in_String_Optimized(s1,s2))  