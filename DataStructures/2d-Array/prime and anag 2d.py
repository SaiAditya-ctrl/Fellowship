start=3
end=1000
a=[[],[]]
l=[]
p=[]
s=set()
for i in range(start,end):
        c=0
        j=2
        while(c==0 and j<i):
            if(i%j)==0:
                c=c+1
            else:
                j=j+1
        if(c==0):
            p.append(i)

def anagram(num1,num2):
    n1=str(num1)
    n2=str(num2)
    if(n1[0] in n2):
        i=n2.index(n1[0])
        if(n1==n2[i:]+n2[0:i]):
            return True
    
        else:
            return False
    else:
        return False
for i in range(0,len(p)):
    for j in range(0,len(p)):
        if(i!=j):
            if(anagram(p[i],p[j])):
                a[0].append(p[i])
            else:
                s.add(p[i])
        else:
            continue

a[1]=list(s)
print('both prime and anagram are ')
print(a)









