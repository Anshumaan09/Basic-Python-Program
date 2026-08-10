def Longest_Substring_k_Repeating_Char(s,k):
    
    if len(s) < k: 
        return 0
    
    frequency = {}
    max_length = 0
    
    for right in range(len(s)):
        current_char = s[right]
        if current_char in frequency:
            frequency[current_char] += 1
        else:
            frequency[current_char] = 1
    
    for right in s:
        if frequency[right] < k:
            left = s.split(right)
        
            for part in left:
                max_length = max(max_length, Longest_Substring_k_Repeating_Char(part,k))
    
    return max_length


str = "aaabb"
k=3
print(Longest_Substring_k_Repeating_Char(str,k))