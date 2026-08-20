class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next


class circularLL:
    def __init__(self, head=None):
        self.head = head

    def insertAtBeg(self, value):
        temp = Node(value)

        # If list is empty
        if self.head is None:
            self.head = temp
            temp.next = self.head
            return

        # Find the last node
        t1 = self.head
        while t1.next != self.head:
            t1 = t1.next

        # New node becomes head
        temp.next = self.head
        t1.next = temp
        self.head = temp

    def insertAtMiddle(self, value, x):
        # If list is empty
        if self.head is None:
            return

        temp = Node(value)
        t1 = self.head

        while True:
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
                return

            t1 = t1.next

            # We have completed one full circle
            if t1 == self.head:
                break

    def printLL(self):
        if self.head is None:
            print("List is empty")
            return

        t1 = self.head

        while True:
            print(t1.data)
            t1 = t1.next

            if t1 == self.head:
                break


# Testing
obj = circularLL()

obj.insertAtBeg(5)
obj.insertAtBeg(10)
obj.insertAtBeg(20)

obj.insertAtMiddle(15, 10)

obj.printLL()