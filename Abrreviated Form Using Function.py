def abbreviated(s):
     st=s[0].upper()
     for i in range(len(s)):
          if(s[i]==" " and s[i+1] not in ('o','O')):
               st=st+s[i+1].upper()
     return st
s=input("Enter The String=")
print("Abbreviated Form Is=",abbreviated(s))
