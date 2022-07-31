n= int(input("Enter a number: "))

temp=n
digit=0
while(n>0):
    a=n%10
    digit= digit + a**3
    n=n//10

if(digit==temp):
    print('Armstrong')
else:
    print("Not Armstrong")