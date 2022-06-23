import time
s=input("Enter A String=")
s=" "+s
l=len(s)
for i in range(l):
    if(s[i]==" "):
         print(s[i+1].upper(),end=" ")
time.sleep(2)
