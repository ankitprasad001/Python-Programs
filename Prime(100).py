#ALL PRIME NUMBERS B/W 1 TO 100
import time
c=0
i=1
while(i<=100):
    c=0
    j=1
    while(j<=i):
        if(i%j==0):
            c=c+1
        j+=1
    if(c==2):
        print(i)
    i=i+1
time.sleep(5)

    
    
    
