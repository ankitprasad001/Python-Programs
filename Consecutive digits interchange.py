a=eval(input("Enter A List With Even Number of elements="))
for i in range(0,len(a),2):
     c=a[i]
     a[i]=a[i+1]
     a[i+1]=c
print(a)
