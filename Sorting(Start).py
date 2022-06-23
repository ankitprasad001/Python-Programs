a=[]
n=int(input("Enter How Many Elemets You Want in the list:-"))
for j in range(0,n):
    k=eval(input("enter a element : - "))
    a.append(k)
print("The List You Created is:-",a)
c=0
l=len(a)
m=a[0]
for i in range(1,l):
    if(a[i]<m):
        m=a[i]
        c=i
print("The Minimum value ,",m,"is situated at:-",c)

    
