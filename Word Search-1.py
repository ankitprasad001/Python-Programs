a=input("Enter A String=")
c=0
s=input("Enter The Word To be searched=")

for i in range(len(a)):
     for j in range(i,len(a)):
          print(a[i:j])
          if (s==a[i:j]):
               c+=1
if c==0:
     print("Not Found")
else:
     print(c,"word found")


