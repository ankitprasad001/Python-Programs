def SI(n):
     i=0
     l=[]
     while(i>=2):
          c=0
          for j in range(1,i+1):
               if(i%j==0):
                    c=c+1
               if(c==2):
                    l.append(i)
               if(len(l)==n):
                    return l
               i=i+1
n=int(input("Enter how many numbers you want="))
print(prime(n))
               
