import sys
sys.path.append("/Users/Aditya/Desktop/functinal/utility")
import utility


f1=open("link1.txt",'w')
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
s=p.print_list()
print(s)
print(p.search('sai'))
p.remove('the')
s1=p.print_list()

print(s1)
print(p.index('abcdef'))
print(p.size())
print(p.isEmpty())

s2=p.print_list()
print(s2)
