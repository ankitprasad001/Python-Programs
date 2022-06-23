n=int(input("Enter No Of Prime Numbers Required="))
count=0
c=0
i=1
while i>=1:
     j=1
     while(j<=i):
          if(i%j==0):
               c=c+1
          j+=1
     if(c==2):
          print(i)
          count=count+1
     if(count==n):
          break
     c=0
     i+=1
     
          
