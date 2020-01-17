n=int(input('enter the number '))
l=[]
s=[2]
for i in range(2,n):
    if(n%i)==0:
        l.append(i)
for i in l:
    count=0
    j=2
    while(count==0 and j<i):
        if(i%j==0):
            count=count+1
        else:
            j=j+1
    if(count==0):
        s.append(i)
print('the prime facotrs for {} are {}'.format(n,s))
    
