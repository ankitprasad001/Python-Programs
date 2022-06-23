print("Palindrome Numbers upto 1000 are")
i=1
while(i<=1000):
    s=0
    n=i
    while(n):
        r=n%10
        s=s*10+r
        n=n//10
    if(s==i):
        print(i)
    i=i+1

        
    
