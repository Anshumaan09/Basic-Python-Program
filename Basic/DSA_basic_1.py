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

# Check if list is sorted
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

lst = [23, 16, 34, 11, 35, 1, 4]
if is_sorted(lst):
    print("The list is sorted.")
else:
    print("The list is not sorted.")

# Move zeros to the end
def move_zeros_to_end(arr):
    non_zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1
    while non_zero_index < len(arr):
        arr[non_zero_index] = 0
        non_zero_index += 1
    return arr

lst2 = [1, 0, 3, 0, 5, 0, 2]
moved_zeros_list = move_zeros_to_end(lst2)
print("List after moving zeros to the end:", moved_zeros_list)