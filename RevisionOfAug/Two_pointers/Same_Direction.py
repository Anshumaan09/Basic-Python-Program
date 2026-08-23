# Brute force
# Move zeros to end
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

nums = [0,1,0,3,12]
for i in range(len(nums)):
    if nums[i] == 0:
        nums.append(nums[i])
        nums.pop(i)
print(nums)

def Move_zeros_Optimal(nums):
    left = 0
    for right in range(len(nums)- 1):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums

print(Move_zeros_Optimal(nums))

