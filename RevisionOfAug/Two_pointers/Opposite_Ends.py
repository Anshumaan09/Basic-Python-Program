# Container with most water
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

def container_with_most_water(nums):
    left = 0
    right = len(nums) - 1
    max_storage = 0
    while left < right:
        # Logic to calculate
        height = min(nums[right], nums[left])
        width = right - left
        total = height * width
        max_storage = max(max_storage, total)

        # Pointer Movement
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1

    return max_storage

height = [1,8,6,2,5,4,8,3,7]
print(container_with_most_water(height))