n=int(input("Enter A Number="))
na=n
s=0
while(n):
     d=n%10
     s=s+d**3
     n=n//10
if(s==na):
     print("Armstrong Number")
else:
     print("Not A Armstrong Number")
     
