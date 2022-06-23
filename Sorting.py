a=[5,2,7,0,1]
l=len(a)
for i in range(0,l-1):
    c=0
    for j in range(i+1,l):
        if(a[i]>a[j]):
            c=a[i]
            a[i]=a[j]
            a[j]=c
print(a)
