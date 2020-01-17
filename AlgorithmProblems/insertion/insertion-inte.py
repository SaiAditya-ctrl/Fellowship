

import sys
sys.path.append("/Users/Aditya/Desktop/functinal/utility")
import utility
file=open("binary.txt",'w')
file.write("hello how are you buddy!")
file.close()
f2=open("binary.txt",'r')
contents=f2.read()
file.close()
l=contents.split(' ')
print('INSERTION SORT')

print('the list of words in file are ',l)

print('before')
s1=utility.insertion_sort(l)

print('the sorted list is ',s1)

