def happy(n,s=0):
     if(s<100):
          while(n):
               d=n%10
               s=s+(d*d)
               n=n//10
          return happy(s,s)
     if(s==100):
          return 1
     if(s>100):
          return 0
n=int(input("Enter A Number="))
if(happy(n)==1):
     print("Happy Number")
else:
     print("Not A Happy Number")

               
          
     
