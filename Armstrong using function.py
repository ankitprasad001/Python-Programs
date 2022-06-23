def armstrong(n):
     na=n
     s=0
     while(n):
          d=n%10
          s=s+d**3
          n=n//10
     if(s==na):
          return 1
     return 0

num=int(input("Enter A Number="))
if(armstrong(num)==1):
     print("Armstrong Number")
else:
     print("Not A Armstrong Number")
     
