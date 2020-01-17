class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if(self.head==None):
            return True
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            temp=self.head
            self.head=Node(data)
            self.head.next=temp
    def pop(self):
        if self.isEmpty():
            return 'No elements'
        else:
            deletenode=self.head
            self.head=self.head.next
            deletenode.next=None
        return deletenode.data
    def peek(self):
        if(self.isEmpty()):
            return 'no elements'
        else:
            return self.head.data
    def display(self):
        temp=self.head
        if(self.isEmpty()):
            print('stack underflow')
        else:
            while(temp!=None):
                print(temp.data)
                temp=temp.next
            return 
s=Stack()
s.push(2)
s.push(3)
s.push(4)
print(s.peek())
s.display()
print(s.pop())
print(s.pop())
print(s.pop())











