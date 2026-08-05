num = int(input("Enter a number: "))
if num > 0:
    print(num, "is a positive number.")
elif num < 0:
    print(num, "is a negative number.")
else:
    print(num, "is zero.")

num2 = int(input("Enter a number: "))
total = 0
for i in range(1, num2+1):
    total += i
print(total)

num3 = int(input("Enter a number: "))
for i in range(1,11):
    print(num3, "x", i, "=", num3*i)

num4 = int(input("Enter a number: "))
for i in range(1, num4+1):
    print(i)

num5 = int(input("Enter a number: "))
num6 = int(input("Enter another number: "))
num7 = int(input("Enter a third number: "))
if num5 > num6 and num5 > num7:
    print(num5, "is the largest number.")
elif num6 > num5 and num6 > num7:
    print(num6, "is the largest number.")
else:
    print(num7, "is the largest number.")