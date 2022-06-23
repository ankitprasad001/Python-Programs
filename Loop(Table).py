#Program To Print The Table Of Any Entered Numbers
i=1
n=int(input("Enter The Number Whose Table is to be printed="))
while i<=10:
    p=n*i
    print(n,"*",i,"=",p,sep='')
    i+=1

