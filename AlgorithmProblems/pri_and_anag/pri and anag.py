import sys
sys.path.append("/Users/Aditya/Desktop/functinal/utility")
import utility



A=[]
p=[]

s=utility.primenumbers1(A,3,1000)
print('the prime and anagram numbers are ')
for i in range(0,len(s)):
    for j in range(0,len(s)):
        if(i!=j):
            if(utility.anagram(s[i],s[j])):
                p.append(s[i])
print(p)

