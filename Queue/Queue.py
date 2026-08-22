class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def insert(self, value):
        self.items.append(value)
        
    def delete(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            return self.items.pop(0)
    
    
Q = Queue()
Q.insert(10)
Q.insert(20)
Q.insert(30)

print(Q.delete())
print(Q.delete())             