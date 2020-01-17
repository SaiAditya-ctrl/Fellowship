exp='(5+6)*(4+3)/(5+6)(7+8)*(7+8)/(4+3)'
print(exp)
import sys
sys.path.append("/Users/Aditya/Desktop/functinal/utility")
from utility import Stack
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



s=Stack()
for i in exp:
    
    s.push(i)
s.print_list()
