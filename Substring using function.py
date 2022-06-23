import time
def substr(s,ss):
     i=0
     while(i<len(s)):
          if(len(ss)+i<=len(s)):
               if(s[i:len(ss)+i]==ss):
                    return 1
          i=i+1

s1=input("Enter Main String=")
s2=input("Enter Sub String To Be Searched=")
k=substr(s1,s2)
if k==1:
     print("Substring Found")
else:
     print("SubString Not Found")

time.sleep(5)
     
