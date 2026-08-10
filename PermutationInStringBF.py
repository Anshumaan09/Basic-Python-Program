from collections import Counter

def permutation_in_String(s1,s2):
    small_string_count = Counter(s1)
    
    window_size = len(s1)
    
    for i in range(len(s2) - window_size + 1):
        
        # 0:0+2 = 0:2
        substring = s2[i:i + window_size]
        
        substring_count = Counter(substring)
        
        if small_string_count == substring_count:
            return True
    
    return False

s1 = "ab"
s2 = "eidboaoo"
print(permutation_in_String(s1,s2))    
    