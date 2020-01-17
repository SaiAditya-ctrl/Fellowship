exp='(5+6)*(4+3)/(5+6)(7+8)*(7+8)/(4+3)'
l=[]
for i in range(0,len(exp)):
    if(exp[0])==')':
        print('not balanced')
        break
    else:
        if(exp[i]=='('):
            l.append('(')
        elif(exp[i]==')'):
            l.pop()
        else:
            continue
if(len(l)==0):
    print('balanced')
      
