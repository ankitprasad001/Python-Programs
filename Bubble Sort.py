a=[15,2,5,19,1]
l=len(a)
for i in range(l-1):
     for j in range(l-i-1):
          if(a[j]>a[j+1]):
               c=a[j]
               a[j]=a[j+1]
               a[j+1]=c
print(a)
