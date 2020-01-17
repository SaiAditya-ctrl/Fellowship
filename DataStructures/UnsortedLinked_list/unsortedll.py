
import sys
sys.path.append("/Users/Aditya/Desktop/functinal/utility")
import utility


f1=open("lin.txt",'w')
f1.write('hello sai aditya we are ready for doing the robbery in the heist')
f1.close()
f2=open("link1.txt",'r')
contents=f2.read()
f2.close()
print(contents)
l=contents.split(' ')
from utility import LinkedList
p=LinkedList()
for i in range(0,len(l)):
    p.adding(l[i])
x=input('enter the string to be esearched')
if(p.search(x)):
    p.remove(x)
else:
    p.adding(x)
l1=p.print_list()
print(l1)
s=' '.join(l1)
f1=open("lin.txt",'w')
f1.write(s)
f1.close()
f2=open("lin.txt",'r')
cont2=f2.read()
f2.close()
print(cont2)
