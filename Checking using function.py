def check(s):
     for i in range(len(s)):
          if s[i].isdigit()==False:
               return 0
     return 1

st=input("Enter A String=")
if(check(st)==1):
     print("Convertible")
else:
     print("Not Convertible")
