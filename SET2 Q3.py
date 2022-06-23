yr=int(input("Enter a Year="))
if(yr<=100):
    if(yr%4==0):
        print("It is a leap year")
    else:
        print("Not a Leap Year")
else:
    if(yr%100==0):
        if(yr%400==0):
            print("Its a leap year + a century")
        else:
            print("It is century but not a leap year")
    else:
        if(yr%4==0):
            print("It is a leap year")
        else:
            print("It ia not a leap year")


        
        
