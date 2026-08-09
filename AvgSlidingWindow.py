def average_of_windows(nums, k):
    avg_lst = []
    windows_sum = sum(nums[:k])
    avg_lst.append(windows_sum/k)
    
    for i in range(k, len(nums)):
        windows_sum += nums[i]
        windows_sum -= nums[i-k]
    
        avg = windows_sum / k
        avg_lst.append(avg)
    
    return avg_lst

nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(average_of_windows(nums,k))
