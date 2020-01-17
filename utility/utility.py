import math
import re
def anagram(n1,n2):
    s=str(n1)
    p=str(n2)
    
    x=s[0]
    if(x in p):
        ind=p.index(x)
        z=p[ind:]+p[0:ind]
        if(s==z):
            return True
        else:
            return False

def primenumbers1(p,s,e):
        
    for i in range(s,e):
        count=0
        j=2
        while(count==0 and i>j):
            if(i%j)==0:
                count=count+1
                j=j+1
            else:
                j=j+1
        if(count==0):
            p.append(i)
    return p
def primenumbers(s,e):
    p=[]
        
    for i in range(s,e):
        count=0
        j=2
        while(count==0 and i>j):
            if(i%j)==0:
                count=count+1
                j=j+1
            else:
                j=j+1
        if(count==0):
            p.append(i)
    return p
def mergesort(l):
    if(len(l)>1):
        mid=len(l)//2
        left_list=l[:mid]
        right_list=l[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=0
        j=0
        k=0
        while(i<len(left_list)and j<len(right_list)):
            if(left_list[i]<right_list[j]):
                l[k]=left_list[i]
                i=i+1
                k=k+1
            else:
                l[k]=right_list[j]
                j=j+1
                k=k+1
        while(i<len(left_list)):
            l[k]=left_list[i]
            i=i+1
            k=k+1
        while(j<len(right_list)):
            l[k]=right_list[j]
            j=j+1
            k=k+1
        return l
def binary_search(l,low,high,x):
    import math
    if(low<high):
        mid=math.floor((low+high)/2)
        print(mid)
    
    
        if(x==l[mid]):
            return l.index(x)
        elif(x>l[mid]):
            binary_search(l,mid,high,x)
        elif(x<l[mid]):
            binary_search(l,0,mid,x)
        elif(x!=l[mid]):
            return 'not found'
    else:
        return 'notfound'

def insertion_sort(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while(j>=0 and key<l[j]):
            l[j+1]=l[j]
            j=j-1
        l[j+1]=key
    return l
def bubble_sort(l):
    for i in range(len(l)):
        for j in range(0,len(l)-i-1):
            if(l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]
    return l
def day_of_week(m,d,y):
    month={1:'January',2:'Feb',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
    day={0:'sun',1:'mon',2:'tue',3:'wed',4:'thu',5:'fri',6:'sat'}
    
    y1=int(y-(14-m)/12)
    x=math.floor(y1+(y1/4)-(y1/100)+(y1/400))
    m1=math.floor(m+(12*(x))*((14-m)/12)-2)
    d1=int(((d+x+31*(m1))/12)% 7)
    return (day.get(d1))
def temperature(n1):
    if(n1=='C'):
        n=int(input('enter here'))
        print('the temperature enetred in centigrade is {}C'.format(n))
        f=(n*(9/5))+32
        print('the temperature after conversion is {}F'.format(f))
    elif(n1=='F'):
        print('the temperature enetred in Farenheit is {}F'.format(n))
        c=(n-32)*(5/9)
        print('the temperature after conversion is {}C'.format(c))
    else:
        print('enter properly')
def payment(p,y,r):
    n=12*y
    
    r1=int(r/(12*100))
    payment=int((p*r)/1-int(math.pow((1+r1),(-n))))
    return payment
def binary(n):
    l=[]
    while(n>1):
        if(n%2)==0:
            l.append(0)
            n=int(n/2)
        else:
            l.append(1)
            n=int(n/2)
    l.append(1)
    return l[::-1]

    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    
    def __init__(self):
        self.head=None
    def adding(self,x):
        if self.head==None:
            self.head=Node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=Node(x)
    def print_list(self):
        l=[]
        tem=self.head
        while(tem):
            l.append(tem.data)
            
            tem=tem.next
        return l
    def search(self,y):
        
        if self.head==None:
            return 'no elements in linked list'
        else:
            temp=self.head
            while(temp.next!=None):
                
                if(temp.data==y):
                    return True
                else:
                    temp=temp.next
            return False
    def remove(self,item):
        
        temp=self.head
        if self.head.data==item:
            self.head=temp.next
            
        else:
            while(temp!=None):
                if temp.data==item:
                    break
                prev=temp
                temp=temp.next
            if(temp==None):
                return
            prev.next=temp.next
            temp=None
    def index(self,item):
        c=0
        temp=self.head
        if self.head.data==item:
            return 0
        else:
            while(temp!=None):
                if(temp.data==item):
                    return c
                else:
                    c=c+1
                    temp=temp.next
            return 'item didnot exist'
    def size(self):
        length=0
        temp=self.head
        while(temp!=None):
            length=length+1
            temp=temp.next
        return length
    def isEmpty(self):
        if(self.head!=None):
            return False
        else:
            return True
    def poping(self):
        if(self.head==None):
            return -1
        else:
            temp=self.head
            while(temp!=None):
                pre=temp
                temp=temp.next
            self.y=temp.data
            pre.next=None
        return self.y
class Queue:
    def __init__(self):
        self.front=self.rear=0
        self.l=[]
    def enQueue(self,p):
        
        self.l.append(p)
        self.rear=self.rear+1
        return self.l
    def deQueue(self):
        self.l.pop(self.front)
        self.front=self.front+1
        return self.l
    def isEmpty(self):
        if self.front==self.rear:
            return True
        else:
            return False
    def size(self):
        c=0
        temp=self.front
        while(temp!=self.rear):
            c=c+1
            temp=temp+1
        return c
class Stack:
    def __init__(self):
        self.l=[]
        self.size=0
    def push(self,item):
        self.l.insert(self.size,item)
        self.size=self.size+1
        
        return self.l
    def poping(self):
        self.l.pop(self.size)
        self.size=self.size-1
        return self.l
    def peek(self):
        return self.l[self.size]
    def isEmpty(self):
        if self.size==0:
            return True
        else:
            return False
    def size(self):
        return self.size
class Deque:
    def __init__(self):
        self.l=[]
        
        self.rear=0
        self.front=0
    def addFront(self,item):
        self.l.append(item)
    def addRear(self,item):
        self.l.insert(0,item)
        
    def removeRear(self):
        return self.l.pop(0)
    def removeFront(self):
        return self.l.pop()
    def isEmpty(self):
        if(len(self.l)==0):
            return True
        else:
            return False
    def size(self):
        return len(self.l)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class HashLinkedList:
    
    def __init__(self):
        self.head=None
    def adding(self,x):
        if self.head==None:
            self.head=Node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=Node(x)
    def print_list(self):
        l=[]
        tem=self.head
        while(tem):
            l.append(tem.data)
            
            tem=tem.next
        return l
def stri(s,user,full_name,contact,date):
    
    s1=re.sub('<<name>>',user,s)
    s2=re.sub('<<full name>>',full_name,s1)
    s3=re.sub('91-xxxxxxxxxx',contact,s2)
    s4=re.sub('01/01/2016',date,s3)
    return s4
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
class Stack:
    def __init__(self):
        self.item=[]
    def push(self,x):
        if x=="(":
            self.item.append(x)
            
        elif x==")":
            if(len(self.item)!=0):
                 print(self.item.pop())
            else:
                print('they are not balanced')
    def print_list(self):
        print(self.item)
        if len(self.item)==0:
            print('the parenthesis are balanced')





