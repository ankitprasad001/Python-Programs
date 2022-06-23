import time
i=1
while(i<=5):
    j=1
    while(j<=5):
        if(j<=i):
            print("*",end=" ")
        j=j+1
    print("\n")
    i=i+1
i=4
while(i>=1):
    j=1
    while(j<=i):
        print("*",end=" ")
        j=j+1
    print("\n")
    i-=1
time.sleep(5)
