import sys
sys.path.append("/Users/Aditya/Desktop/functinal/utility")
import utility


f=open("hash.txt",'w')
f.write('1 12 13 37 66 77 78 88 90 91')
f.close()
f1=open("hash.txt",'r')
cont=f1.read()
print(cont)
f1.close()
l=cont.split(' ')
s=[0,0,0,0,0,0,0,0,0,0]
from utility import HashLinkedList
p=HashLinkedList()

for i in range(0,len(l)):
    ind=int(int(l[i])%11)
    print(ind)
    s[ind]=HashLinkedList()
    s[ind].adding(l[i])
    print(s[ind].print_list())
    
for i in range(len(s)):
    print(s[i])
    
    
    
