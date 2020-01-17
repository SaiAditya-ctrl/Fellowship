import sys
sys.path.append("/Users/Aditya/Desktop/functinal/utility")
import utility

from utility import Deque
s=input('enter the string')
li=[]
d=Deque()
for i in s:
    d.addRear(i)
for i in range(len(s)):
    li.append(d.removeRear())
print(li)
if(s==''.join(li)):
    print('it is palindrome')
else:
    print('not palindrome')
