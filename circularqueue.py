def enqueue(li):
     global rear
     global front
     if(front==0 and rear==len(li)-1) or front==rear+1:
          print("Overflow")
     elif rear==-1:
          rear=front=0
          li[rear]=int(input("Enter The Value="))
     elif rear==len(li)-1:
          rear=0
          li[rear]=int(input("Enter The Value="))
     else:
          rear=-1
          li[rear]=int(input("Enter The Value="))

def dequeue(li):
     global rear
     global front
     if front==-1:
          print("Underflow")
     elif rear==front:
          print("The deleted element is=",li[front])
          rear=front-1
     elif front==len(li)-1:
          print("The deleted element is=",li[front])
          front=0
     else:
          print("The deleted element is=",li[front])
          front+=1

def traverse(li):
     if(front==-1):
          print("No element")
     else:
          if(front<=rear):
               for i in range(front,rear+1):
                    print(li[i])
          else:
               for i in range(front,len(li)):
                    print(li[i])
               for i in range(rear+1):
                    print(li[i])
#main
n=int(input("How mant elements you want to enter in the list="))
li=[0]*n
front=rear=-1
ch='y'
while ch!=4:
     print("The Options are as follows:-")
     print("1.Enqueue")
     print("2.Dequeue")
     print("3.Traverse")
     print("4.Exit")
     ch=int(input("Enter Your Choice:-"))
     if ch==1:
          enqueue(li)
     elif ch==2:
          dequeue(li)
     elif ch==3:
          traverse(li)
     elif ch>4:
          print("Invalid Input")




          
          
