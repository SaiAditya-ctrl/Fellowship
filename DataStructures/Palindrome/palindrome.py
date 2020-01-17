l=[]
def palindrome(s):
    if(len(s)>1):
        for i in range(0,len(s)):
            if(i==0):
                print((s[0]+palindrome(s[1:])))
                print(l)
                print((s[0]+palindrome(s[-1:0:-1])))
            
            
            elif(i==len(s)-1):
                l.append(s[i]+s[0:i])
            else:
                l.append(s[i:]+s[0:i])
    elif(len(s)==1):
        return s
    elif(len(s)==0):
        return ''
print(l)
palindrome('abc')
print(l)
