def greet():
    print("Hello, Gpt Welcome to python")

greet()

def add(a,b):
    return a+b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = add(a, b)
print(result)

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_even(num):
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num2 = int(input("Enter a number: "))
fact = factorial(num2)
print("Factorial of", num2, "is", fact)

def reverse(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

num4 = int(input("Enter a number: "))
reversed_num = reverse(num4)
print("Reversed number is:", reversed_num)
