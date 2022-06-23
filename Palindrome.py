n=int(input("Enter A number:-"))
na=n
r=0
while(n):
     d=n%10
     r=(r*10)+d
     n=n//10
if(r==na):
     print("palindrome")
else:
     print("not palindrome")

     
