#Progarm to print the discounted amount
amt=int(input("Enter Total Amount="))
if(amt>15000):
    d=20
if(amt>5000 and amt<=15000):
    d=15
if(amt>=2000 and amt<=5000):
    d=10
if(amt<2000):
    d=5
D=amt-(amt*d/100)
print("Discounted Amount=",D)

        
    
    
