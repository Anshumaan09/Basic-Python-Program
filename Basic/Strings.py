# Brute force
var = input("Enter a string: ")
for char in (var,var[::-1]):
    print(char)

# Easy
print(var[::-1])

def count_vowels(str):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in str:
        if char in vowels:
            count += 1
    return count

Str1 = "education"
vowel_count = count_vowels(Str1)
print("The number of vowels in the string is:", vowel_count)

def pallindrome_check(str):
    return str == str[::-1]

str2 = "madam"
if pallindrome_check(str2):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


def count_character_frequency(str):
    frequency = {}
    for char in str:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

str4 = "banana"
print("Character frequency in the string is:", count_character_frequency(str4))