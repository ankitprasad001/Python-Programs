n=int(input("Enter Number Of palindrome you want="))
i=1
r=0
c=0
print("The palindrome Numbers Are:-")
while(i>=1):
     na=i
     while(na):
          d=na%10
          r=r*10+d
          na=na//10
     if(r==i):
          print(i)
          c=c+1
     if(c==n):
          break
     r=0

     i=i+1
     
          
     
     
