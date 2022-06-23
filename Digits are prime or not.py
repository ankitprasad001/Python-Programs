c=0
n=int(input("Enter A Number="))
co=0
while(n):
     d=n%10
     i=1
     while(i<=d):
          if(d%i==0):
               c+=1
          i+=1 
     if(c==2):
          print(d)
          co+=1
          
     c=0
     n=n//10
if(co==0):
     print("Number Does Not Contain Any Prime Numbers")
     
