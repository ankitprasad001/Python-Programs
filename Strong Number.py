n=int(input("Enter A Number="))
na=n
s=0
while(n):
     d=n%10
     f=1
     for i in range(1,d+1):
          f=f*i
     s=s+f
     n=n//10
if(s==na):
     print("Strong Number")
else:
     print("Not A Strong Number")
     
     
