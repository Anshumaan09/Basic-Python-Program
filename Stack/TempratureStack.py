# Brute force

def tempStackBF(temp):
    lst = [0] * len(temp) 
    for i in range(len(temp)-1):
        for j in range(i+1, len(temp)):
            if temp[j] > temp[i]:
                lst[i] = j-i
                break
            
    return lst

def tempStackOpt(temperatures):
    result = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day

        stack.append(i)

    return result
        

temprature = [73,74,75,71,69,72,76,73]
print(tempStackOpt(temprature))
# o/p = [1,1,4,2,1,1,0,0]