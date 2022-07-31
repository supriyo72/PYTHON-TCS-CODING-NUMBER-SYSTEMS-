n= int(input("Enter a no: "))

temp=n
rev=0
while(n>0):
    rev= rev*10 + n%10
    n=n//10

if(rev==temp):
    print("pall")
else:
    print("Not pall")
