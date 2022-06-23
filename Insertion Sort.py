def insort(ar):
     for i in range(len(ar)):
          temp=ar[i]
          j=i-1
          while temp<ar[j] and j!=-1:
               ar[j+1]=ar[j]
               j=j-1
          ar[j+1]=temp
     return ar

ar=eval(input("Enter The List="))
print("Sorted List\n",insort(ar))
