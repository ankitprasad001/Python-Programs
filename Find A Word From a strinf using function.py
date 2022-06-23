def find(s,w):
     l=s.split()
     for i in l:
          if(i==w):
               return True
     return False

s=input("Enter The String=")
w=input("Enter The Word To Be Searched In The String=")
if(find(s,w)==True):
     print("Found")
else:
     print("Not Found")
