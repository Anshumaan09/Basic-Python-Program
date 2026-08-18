# We are making a class because data type khud ka banana hai
class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next

class SinglyLinkedlist:
    def __init__(self, head=None):
        self.head = head
    
    def insertAtEnd(self, value):
        temp = Node(value) # automatically assign next as None
        if self.head != None:
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
        
            t1.next = temp # Link with temp which is at last position
        else:
            self.head = temp
    
    def insertAtBeg(self, value):
        temp = Node(value) # Node created
        temp.next = self.head
        self.head = temp
        
    def insertAtMid(self, value, x): # x is for search so that we can add the value after x
        temp = Node(value)
        t1 = self.head
        
        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next
    
    def deleteLL(self, value):
        t1 = self.head
        prev = t1
        if(t1.data == value):
            self.head = t1.next
        
        while(t1.next != None):
            if(t1.data == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
        if(t1.data == value):
            prev.next = None
            
    def reverseLL(self):
        prev = None
        current = self.head
        
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
        
    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)
        
obj = SinglyLinkedlist()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertAtMid(40,20)
obj.deleteLL(30)
obj.insertAtMid(25,20)
obj.reverseLL()
obj.printLL()