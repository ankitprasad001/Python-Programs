i=1
while(i<=7):
     j=1
     while(j<=7):
          if(i==1 or i==7 or i+j==8):
               print("*",end=" ")
          else:
               print(" ",end=" ")
          j=j+1
     print()
     i=i+1
