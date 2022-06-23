a={}
s={}
i=1
while(i<=3):
     name=input("Enter Name=")
     roll=int(input("Enter Roll Number="))
     marks=int(input("Enter Total Marks of 5 subjects out of 500="))
     s={name:{"Roll":roll,"Marks":marks}}
     a.update(s)
     i=i+1
print(a)
