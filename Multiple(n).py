#Program to print as many multiples of any number as required by user
n=int(input("Enter A Number whose multiples are required="))
m=int(input("Enter The Number of multiples required="))
i=1
while(i<=m):
    p=n*i
    print(p,end="\n")

    i=i+1

    
