import sys
sys.path.append("/Users/Aditya/Desktop/functinal/utility")
import utility
def mergesort(l):
    if(len(l)>1):
        mid=len(l)//2
        left_list=l[:mid]
        right_list=l[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=0
        j=0
        k=0
        while(i<len(left_list)and j<len(right_list)):
            if(left_list[i]<right_list[j]):
                l[k]=left_list[i]
                i=i+1
                k=k+1
            else:
                l[k]=right_list[j]
                j=j+1
                k=k+1
        while(i<len(left_list)):
            l[k]=left_list[i]
            i=i+1
            k=k+1
        while(j<len(right_list)):
            l[k]=right_list[j]
            j=j+1
            k=k+1
        return l


s='hello sai aditya how are you'
print('the unsorted string is ',s)
l=s.split(' ')
print('the sorted string is ')
print(mergesort(l))
       
