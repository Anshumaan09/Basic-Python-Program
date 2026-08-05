lst = []
lst.append(12)
lst.append(10)
lst.append(8)
lst.append(85)
lst.append(72)
print("The list is:", lst)
print("The first element is:", lst[0])
print("The last element is:", lst[-1])


add = 0
for i in lst:
    add+= i
print("The sum of the elements in the list is:", add)

largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print("The largest element in the list is:", largest)
    
lst.sort()
print(lst[-1])

for i in lst:
    if i % 2 == 0:
        print(i, "is an even number.")
    else:
        print(i, "is an odd number.")

for i in range(len(lst), 0, -1):
    print(lst[i-1], end=" ")