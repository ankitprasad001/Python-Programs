a=eval(input("Enter A List="))
c=0
w=eval(input("Enter The Element to be searched for="))
for i in range(len(a)-1):
     if(w==a[i]):
          print("Found At index",i)
          c=c+1
if(c==0):
     print("Not Found")
     
