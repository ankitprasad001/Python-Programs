def LCM(n1,n2,i=1):
     if(n1==1 or n2==1):
          return n1*n2
     if(i%n1==0 and i%n2==0):
          return i
     return LCM(n1,n2,i+1)

a=int(input("Enter 1st Number="))
b=int(input("Enter 2nd Number="))
print("The LCM of ",a,'and',b,'is=',LCM(a,b))
