c=1
i=4
while(i>=1):
    j=1
    while(j<=4):
        if(j>=i):
            print(c," ",end=" ")
            c=c+1
        else:
            print(" ",end=" ")
        j=j+1
    print("\n")
    i=i-1
