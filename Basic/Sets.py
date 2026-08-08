def find_duplicates(lst):
    set1 = set()
    duplicates = set()
    for i in lst:
        if i in set1:
            duplicates.add(i)
        else:
            set1.add(i)
    return list(duplicates)

def find_duplicate_bool(lst):
    set1 = set()
    for i in lst:
        if i in set1:
            return True
        else:
            set1.add(i)
    return False

lst = [1, 2, 3, 4, 5, 1, 2, 6]
duplicates = find_duplicates(lst)
dup = find_duplicate_bool(lst)
print("Are there duplicates in the list?", dup)
print("Duplicates in the list:", duplicates)

def non_repeated_characters(str):
    str = str.lower()
    char_count = {}
    non_repeated = []
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    for char in char_count:
        if char_count[char] == 1:
            non_repeated.append(char)
            break
        
    return non_repeated

String = "Swiss"
print("Non-repeated characters in the string:", non_repeated_characters(String))

def Anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    dict1 = {}
    dict2 = {}
    
    for char in str1:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1
    
    for char in str2:
        if char in dict2:
            dict2[char] += 1
        else:
            dict2[char] = 1
    
    if dict1 == dict2:
        return True
    else:
        return False

str1 = "Silent"
str2 = "Listen"
check_anagram = Anagram(str1, str2)
if check_anagram:
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")
    

def remove_duplicates(str):
    str = str.lower()
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    if char_count.items() != 1:
        return ''.join(char_count.keys())
    else:
        return str
    
str1 = "Programming"
print("String after removing duplicates:", remove_duplicates(str1))