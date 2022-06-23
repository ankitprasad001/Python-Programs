import time
i=1
c=0
c1=0
n=int(input("Enter Number Of Prime Numbers Required="))
while(i>=0):
    c=0
    j=1
    while(j<=i):
       if(i%j==0):
           c=c+1
       j=j+1
    if(c==2):
        print(i)
        c1=c1+1
    if(c1==n):
        break
    i=i+1
time.sleep(2)
