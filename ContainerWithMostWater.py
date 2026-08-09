from typing import List

def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_storage = 0
    while left < right:
        w = right - left
        h = min(height[left], height[right])
        curr_storage = w*h
        max_storage = max(max_storage,curr_storage)
        if height[left] < height[right]:
            left+=1
        else :
            right-=1
    return max_storage

height = [1,8,6,2,5,4,8,3,7]
max_area = maxArea(height)
print("maximum" , max_area)