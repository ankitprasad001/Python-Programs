def palin(n):
     na=n
     r=0
     while(na):
          d=na%10
          r=r*10+d
          na=na//10
     if(r==n):
          return 1
     return 0
num=int(input("Enter The Number="))
if(palin(num)==1):
     print("Palindrome")
else:
     print("Not Palindrome")
