year=int(input("Enter the year"))

if(year%400==0):
    print("the {} is leap year".format(year))

elif(year%100!=0 and year%4==0):
    print("the {} year is a leap year".format(year))
else:
    print("the {} year is not leap year".format(year))

