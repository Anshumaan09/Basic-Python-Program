from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    windows_sum = sum(nums[:k])
    max_sum = windows_sum
    
    # Slide the window
    for i in range(k, len(nums)):
        windows_sum += nums[i]
        windows_sum -= nums[i-k]
        max_sum = max(max_sum,windows_sum)
        
    avg = max_sum/k
    return avg

nums = [5]
k =1
print("maximum average", findMaxAverage(nums,k))

def maxSubArray(nums,k):
    subArraySum = sum(nums[:k])
    maxSubArraySum = subArraySum
    
    for i in range(k, len(nums)):
        subArraySum += nums[i]
        subArraySum -= nums[i-k]
        maxSubArraySum = max(maxSubArraySum, subArraySum)
    
    return maxSubArraySum

nums = [2, 1, 5, 1, 3, 2] 
k = 3
print("Maximum Sub Array", maxSubArray(nums,k))