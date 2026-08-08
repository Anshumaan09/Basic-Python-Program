def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]

arr = [2, 7, 11, 15]
target = 13
result = two_sum(arr, target)
if result:
    print("Indices of the two numbers that add up to the target:", result)  
else:
    print("No two numbers add up to the target.")