# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


nums = [4, 7, 1, 9, 3]
target = 9
result = linear_search(nums, target)
if result == -1:
    print("Element not found in the list.")
else:
    print("Element found at index:", result)


# Count Occurance
def count_occurrences(arr, target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            count += 1
    return count

nums2 = [1, 2, 3, 4, 2, 5, 2]
target2 = 2
occurrences = count_occurrences(nums2, target2)
print("The number", target2, "occurs", occurrences, "times in the list.")

def second_largest(arr):
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num
    return second if second != float('-inf') else None

nums5 = [10, 5, 8, 12, 3]
second_largest_num = second_largest(nums5)
if second_largest_num is not None:
    print("The second largest number in the list is:", second_largest_num)
            