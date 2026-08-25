from collections import Counter

def uniqueCharBF(s):
    s = s.lower()
    
    for i in range(len(s)):
        count = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1

        if count == 1:
            return i

    return -1

s = "aJava"
print(uniqueCharBF(s))

def uniqueCharOpt(s):
    s = s.lower()
    freq = Counter(s)
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i
    return -1

s = "Amamn"
print(uniqueCharOpt(s))