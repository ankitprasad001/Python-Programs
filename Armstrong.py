n=int(input("Enter A Number="))
na=n
r=0
while(n):
    s=n%10
    r=r*10+(s**3)
    n=n//10
if(s==na):
    print("Armstrong")
else:
    print("Not Armstrong")

