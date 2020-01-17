n=int(input('enter how many persons you want to add'))
import sys
sys.path.append("/Users/Aditya/Desktop/bridge/Programming/Functional")
from anag import Queue

q=Queue()
l=[2000,3000,1000]
Principle=sum(l)
s=[]
for i in range(0,n):
    q.enQueue(input('enter name of person'))
    

def check():
        
        for i in range(0,n):
            choice=input('Deposit means D or Withdrwal means W ')
            if choice=='D':
                deposit(i)
                q.deQueue()
                i=i+1
            elif choice=='W':
                withdraw(i)
                q.deQueue()
                i=i+1


def deposit(i):  
        n1=int(input('enter how much money you want to deposit'))
        global l
        l[i]=l[i]+n1
        print(l[i])
        s.append(l[i])
      
def withdraw(i):
     n1=int(input('enter how much money you want to deposit'))
     global l
     
     if(l[i]>=n1):
         l[i]=l[i]-n1
         print(l[i])
         s.append(l[i])
        
     else:
        print('insufficent funcds in your account so please enter the amount below')
print(Principle)
print(l)
check()
print(s)
print(sum(s))
print(l)
print(sum(l))

