a=0
b=1
print(a,b,sep="\n")

for i in range(20):
     c=a+b
     print(c,sep="\n")
     a=b
     b=c
