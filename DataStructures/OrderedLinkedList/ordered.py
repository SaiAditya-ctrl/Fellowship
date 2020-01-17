                      
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class OrderedLinkedList:
    def __init__(self):
        self.head=None
    def add(self,x):
        if(self.head==None):
            self.head=Node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=Node(x)
    def printing(self):
        if(self.head)==None:
            print('no elements in linked list')
        else:
            temp=self.head
            while(temp!=None):
                print(temp.data)
                temp=temp.next
        
    def sorting(self):
        curr=self.head
        after=None
        if(self.head)==None:
            print('no elements in the list')
        else:
            while(curr!=None):
                after=curr.next
                while(after!=None):
                    if(curr.data>after.data):
                        temp=curr.data
                        
                        curr.data=after.data
                        after.data=temp
                    after=after.next
                curr=curr.next
    def duplicate(self):
        if(self.head)==None:
            print('no ele in linkedlist')
        else:
            temp=self.head
            while(temp.next!=None):
                if(temp.data==temp.next.data):
                    new=temp.next.next
                    temp.next=None
                    temp.next=new
                    temp=temp.next
                else:
                    temp=temp.next


o=OrderedLinkedList()
o.add(9)
o.add(2)
o.add(1)
o.add(5)
o.add(2)
o.printing()
o.sorting()
o.printing()
o.duplicate()
o.printing()
