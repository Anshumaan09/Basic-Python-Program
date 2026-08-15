def MatrixSearch(nums, target):
    row = len(nums)
    column = len(nums[0])
    left = 0
    right = (row*column) - 1
    while left <= right:
        mid = left + (right - left)//2
        # convert back to row and column as it is in index format
        r = mid // column
        c = mid % column
        value = nums[r][c]
        if value == target:
            return mid
        elif value > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 23
print(MatrixSearch(matrix, target))