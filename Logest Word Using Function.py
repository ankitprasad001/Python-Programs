def longest(s):
     l=s.split()
     m=l[0]
     for i in l:
          if(len(i)>len(m)):
               m=i
     return m

s=input("Enter A String=")
print("Longest Word=",longest(s))
