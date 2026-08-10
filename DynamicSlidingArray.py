def dynamicSlidingWindow(s):
    start = 0
    seen = set()
    max_len = 0
    
    for end in range(len(s)):
        while s[end] in seen:
            seen.remove(s[end])
            start +=1
        
        seen.add(s[end])
        
        curr_len = end - start + 1
        max_len = max(max_len, curr_len)
    return max_len

s = "abcabcbb"
print(dynamicSlidingWindow(s))