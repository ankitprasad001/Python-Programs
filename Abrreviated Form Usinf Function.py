def abbreviated(s):
     s=''
     for i in range(len(s)):
          if(s[i]==" "):
               st=st+s.upper(s[i+1])

          
          return st
s=input("Enter The String=")
print("Abbreviated Form Is=",abbreviated(s))
