a=input("Enter A String=")
a=a+" "
l=len(a)
n=input("Enter The Word to be searched=")
n=n+" "
s=''
c=0
for i in range(l):
     s=s+a[i]
     if(a[i]==" "):
          if(s==n):
               c=c+1
          s=''
if(c==0):
     print("Word Not Found")
else:
     print("The word has been found ",c,"times")

          
     
