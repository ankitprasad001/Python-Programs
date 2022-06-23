def pow(x,n):
     if(n==1):
          return x
     a=return pow(x,n-1)+x

x=int(input("Enter The Number="))
n=int(input("Enter Till Where The Table Will be Printed for the above number="))
if n==0:
     print("Table of 0 Is Not possible")
else:
     print("The Table of ",x,"till",n,"is:-",pow(x,n))
