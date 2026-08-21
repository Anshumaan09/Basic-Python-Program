class stack:
    def __init__(self):
        self.lst = []
    
    def length(self):
        return len(self.lst)
    
    def push(self, value):
        self.lst.insert(0, value)
        
    def peek(self):
        if len(self.lst) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.lst[0]
    
    def pop(self):
        if len(self.lst) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.lst.pop(0)
        

obj = stack()
obj.push(10)
obj.push(20)
obj.push(30)
print(obj.peek())
print(obj.pop())
print(obj.peek())