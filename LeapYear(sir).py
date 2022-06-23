yr=82
lc=0
i=1
c=1
l=1
while(i<=82):
    
    if(yr%100==0):
        if(yr%400==0):
            lc=lc+1
    else:
        if(yr%4==0):
            l=l+1
    i=i+1
    yr=yr+1
print("Number Of Leap Year You Will See=",l)
print("Number Of Leap Year + Century=",lc)
