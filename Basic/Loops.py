for i in range(1,5):
    for j in range(1,5):
        print("*", end="")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end="")
    print()

num1 = int(input("Enter a number: "))
for i in range(num1, 0, -1):
    print(i)


num2 = int(input("Enter a number: "))
count = 0
while num2 > 0:
    num2 //= 10
    count += 1
print("The number of digits in the number is:", count)


num3 = int(input("Enter a number: "))
total = 0
while num3 > 0:
    digit = num3 % 10
    total += digit
    num3 //= 10
print(total)