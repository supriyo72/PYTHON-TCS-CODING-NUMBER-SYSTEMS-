num= int(input("Enter a no: "))

temp=0

for i in range(2,num):
      if(num%i==0):
           temp=temp+1
           
if(temp>0):
    print("Not Prime")
else:
    print("Prime")