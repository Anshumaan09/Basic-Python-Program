class MinStack1:

    def __init__(self):
        self.lst = []

    def push(self, value: int) -> None:
        self.lst.insert(0,value)

    def pop(self) -> None:
        if len(self.lst) == 0:
            raise Exception("Empty Stack")
        else:
            self.lst.pop(0)

    def top(self) -> int:
        if len(self.lst) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.lst[0]
        

    def getMin(self) -> int:
        return min(self.lst)

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(
                min(value, self.min_stack[-1])
            )

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(0)
obj.push(5)
obj.push(6)
obj.push(2)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()