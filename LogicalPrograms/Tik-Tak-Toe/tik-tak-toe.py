import random
import winner
l=[0,1,2,3,4,5,6,7,8]
p1=[0,1,2,3,4,5,6,7,8]

for i in range(0,4):
    
        print('select one number from the given list')
        print(p1)
        a=int(input('eneter'))
        ind=p1.index(a)
        p1[ind]=9
        l[ind]='C'
        
        
    
        print('selec')
        print(l)
        print(p1)
        x=int(input('enter numbers'))
        ind1=p1.index(x)
        p1[ind1]=9
        l[ind1]='P'
for i in range(len(p1)):
    if(p1[i]!=9):
        l[i]='P'
        
        
print(l)
i=0
print(l[i+3])
def winner1(l):
    i=0
    p=0
    while(p<3):
        if(l[i]=='C' and l[i+1]=='C' and l[i+2]=='C'):
            print('player C won')
            return 'C won'
            
        elif(l[i]=='P'and l[i+1]=='P' and l[i+2]=='P'):
            print('player P won')
            return 'Awon'
        i=i+3
        p=p+1
def winner2(l):
    i=0
    p=0
    while(p<3):
        if(l[i]=='C' and l[i+3]=='C' and l[i+6]=='C'):
            print('player C won')
            return 'C won'
            
        elif(l[i]=='P' and l[i+3]=='P' and l[i+6]=='P'):
            print('player P won')
            return 'Awon'
        i=i+1
        p=p+1
def winner3(l):
    i=0
    if(l[i]=='C' and l[i+4]=='C' and l[i+8]=='C'):
        print('player C won')
        return 'C won'
    elif(l[i+2]=='P' and l[i+4]=='P' and l[i+6]=='P'):
        print('player P won')
        return 'Pwon'
print(winner1(l))
print(winner2(l))
print(winner3(l))

