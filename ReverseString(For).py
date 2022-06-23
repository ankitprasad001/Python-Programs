r=" "
n=input("Enter Name:")
l=len(n)-1
for i in range(0,(l//2)+1):
    n[i]=n[l]
    l=l-1
print(n)
