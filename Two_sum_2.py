def twoSumSorted(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        sum_value = arr[left] + arr[right]
        if sum_value == target:
            return [left,right]
        elif sum_value < target:
            left += 1
        else:
            right -=1
    return []

arr = [1,3,8,11,13]
target = 11
print(twoSumSorted(arr,target))