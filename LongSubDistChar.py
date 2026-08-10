def LongSubsDistChar(arr,k):
    left = 0
    max_length = 0
    char_stored = {}
    
    for right in range(len(arr)):
        current_char = arr[right]
        if current_char in char_stored:
            char_stored[current_char] += 1
        else:
            char_stored[current_char] = 1
        
        
        while len(char_stored) > k:
            left_char = arr[left]
            char_stored[left_char] -=1
            
            if char_stored[left_char] == 0:
                del char_stored[left_char]
            
            left +=1
        
        curr_length = right - left + 1
        max_length = max(max_length, curr_length)
    return max_length

str = "ececba"
k = 2
print(LongSubsDistChar(str,k))