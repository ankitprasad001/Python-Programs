c1=0
c=0
i,j=1,1
s=0
while(i>=1):
     j=1
     while(j<=i):
          if(i%j==0):
               c+=1
          j+=1
     if(c==2):
          s=i%10
          if(s==1):
               print(i)
               c1=c1+1
     if(c1==15):
          break
     i+=1
     c=0
     s=0
