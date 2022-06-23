def rev(n,s=0):
     if(n==0):
          return s
     return rev(n//10,s*10+(n%10))

n=int(input("enter a number="))
print("The Number in reversed form is=",rev(n))
