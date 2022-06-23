r=0
n=int(input("Enter A Number="))
while(n):
     d=n%10
     r=(r*10)+d
     n=n//10
print("REverse of the number is=",r)
