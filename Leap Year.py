yr=int(input("Enter A Year="))
if(yr<=100):
    if(yr%4==0):
        print("Leap Year")
    else:
        print("Not A Leap Year")
else:
    if(yr%100==0):
        if(yr%400==0):
            print("Leap Year and Century Too")
        else:
            print("Century but not a leap Year")
    else:
        if(yr%4==0):
            print("Leap Year But Not A Century")
        else:
            print("Not A Leap Year")


            
