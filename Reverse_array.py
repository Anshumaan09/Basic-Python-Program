# Reverse Array in place
# Two pointer approach to reverse an array in place
def reverse_in_place(nums):
    left, right = 0, len(nums) -1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums

# Example usage
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
reversed_arr = reverse_in_place(arr)   
print("Reversed array:", reversed_arr)