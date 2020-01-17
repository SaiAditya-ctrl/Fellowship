n=int(input('enter the dead end for n'))
sum=0
for i in range(1,n+1):
    sum=sum+(1/i)

print(round(sum,ndigits=2))
