n=int(input("Enter A Number="))
c=0
t=1
sq=n*n
s=0
while(sq):
     d=sq%10
     s=s+d*t
     t=t*10
     if(s==n):
          c=1
          break
     sq=sq//10
if(c==1):
     print("Automorphic Number")
else:
     print("Not Automorphic Number")
     
