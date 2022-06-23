def push(l):
     global top

     if top==len(l)-1:
          print("Overflow")

     else:
          top=top+1
          l[top]=int(input("Enter The Value="))

def pop(li):
     global top

     if top==-1:
          print("UnderFLow")

     else:
          print("Deleted Element Is=",li[top])
          top=top-1

def display(l,top):
     if top==-1:
          print("No Element")

     else:
          for i in range(len(l),-1,-1):
               print(l[i])

# main
n=int(input("Enter Size Of The List="))
l=[0]*n
top=-1
while True:
     print("The Options are:-")
     print("1.Push\n2.Pop\n3.Traversing\n4.Exit")
     i=int(input("Enter your choice="))
     if i==1:
          push(l)
     elif i==2:
          pop(l)
     elif i==3:
          display(li,top)
     else:
          exit()
          
          
          
          
          
