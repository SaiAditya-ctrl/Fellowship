import sys
sys.path.append("/Users/Aditya/Desktop/functinal/utility")
import utility

s='Hello <<name>>, We have your fullname as <<full name>>in pur system. our contact is 91-xxxxxxxxxx.please, let us know incase of any clarification.THankYoy bridgelabz 01/01/2016'
import re
user=input('enter name')
full_name=input('enter name')
contact=input('enter contect')
date=input('enter todays data')
import utility
print(utility.stri(s,user,full_name,contact,date))
