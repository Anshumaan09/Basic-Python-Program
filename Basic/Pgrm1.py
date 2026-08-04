print("My name is Anshumaan")
print("I am learning Python")

print("Input:")
a = 5
b = 7
sum = a + b
print(sum)

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("Area of the rectangle:", area)

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a>b:
    print(a, "is greater than", b)
else:
    print(b, "is greater than", a) 