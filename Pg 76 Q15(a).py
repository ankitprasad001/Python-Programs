i=1
while(i<=7):
     j=1
     while(j<=7):
          if(i==1 or i==7 or j==i):
               print("*",end=" ")
          else:
               print(" ",end=" ")
          j+=1
     print()
     i+=1
