n=int(input("Enter Number of Automorphic Numbers Required="))
i=1
count=0
while(i>=1):
     c=0
     t=1
     sq=i*i
     s=0
     while(sq):
          d=sq%10
          s=s+d*t
          t=t*10
          if(s==i):
               c=1
               break
          sq=sq//10
     if(c==1):
          print(i)
          count+=1
     if(count==n):
          break
     i=i+1

          
     
     
