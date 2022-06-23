for n in range(1,21):
     c=0
     t=1
     sq=n*n
     s=0
     while(sq):
          d=sq%10
          s=s+d*t
          t=t*10
          if(s==n):
               c=1
               break
          sq=sq//10
     if(c==1):
          print(n)
     
     
