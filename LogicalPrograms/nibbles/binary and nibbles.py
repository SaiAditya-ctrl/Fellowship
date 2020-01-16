import sys
sys.path.append("/Users/Aditya/Desktop/functinal/utility")
import utility



n=int(input('eneter number'))

s=utility.binary(n)
print(s)
while(len(s)!=8):
    s.insert(0,0)
s[0:4],s[4:]=s[4:],s[0:4]
print(s)
l=s[::-1]
print(l)
sum1=0
for i in range(0,len(l)):
    sum1=sum1+l[i]*(2**i)
print(sum1)
