a=eval(input("Enter A List;-"))
l=len(a)
for i in range(l-1):
     for j in range(i+1,l):
          if(a[i]>a[j]):
               c=a[i]
               a[i]=a[j]
               a[j]=c
print(a)
