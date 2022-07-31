n=int(input("Enter a number: "))

temp=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
    
if(temp%sum==0):
    print("The no is Harshad")
else:
    print("Not harshad")