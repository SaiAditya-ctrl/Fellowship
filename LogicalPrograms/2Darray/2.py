l=[0,1,0,-1,1,2,-2,1,3,4,-4,-3,-1]
s=[]
for i in range(0,len(l)):
    for j in range(1,len(l)):
        for k in range(2,len(l)):
            if(l[i]+l[j]+l[k]==0):
                s.append([i,j,k])
print(s)
print(len(s))

