def LCM(n1,n2):
     for i in range(1,(n1*n2)+1):
          if(i%n1==0 and i%n2==0):
               return i

a=int(input('Enter 1st Number='))
b=int(input('Enter 2nd Number='))
print("LCM of the numbers is=",LCM(a,b))
