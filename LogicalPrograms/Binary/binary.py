n=int(input('enetr number for conversion '))
s=''

import anag
p=anag.binary(n)
print(p)
for i in p:
    print(i,end='')
    
