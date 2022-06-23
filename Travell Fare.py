#Program To Calculate Fare
dis=int(input("Enter Distance To Be travelled="))
noc=int(input("Enter Number of children travelling="))
noa=int(input("Enter Number of adult travelling="))
if(dis>=1000):
    f=1000
elif(dis>=500):
    f=500
elif(dis>=200):
    f=300
else:
    f=200
f=(noa*f)+(f/2*noc)
print("Fare to be paid=",f)
