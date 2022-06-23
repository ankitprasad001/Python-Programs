n1=int(input("Enter 1st Number="))
n2=int(input("Enter 2nd Number="))
p=n1*n2
for i in range(1,p+1):
    if(i%n1==0 and i%n2==0):
        print("The LCM of the digits is=",i)
        break

