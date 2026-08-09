def sorted_squares(nums):
    left = 0
    right = len(nums) - 1
    square_lst = []
    while left < right:
        square_lst.append(nums[left]**2)
        square_lst.append(nums[right]**2)
        left +=1
        right -=1
        if left == right:
            square_lst.append(nums[right]**2)
    
    square_lst.sort()
    return square_lst

nums = [-4,-1,0,3,10]
print(sorted_squares(nums))