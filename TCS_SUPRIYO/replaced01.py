n=int(input("Enter a no: "))
num=0
if n==0:
    num=1
while(n>0):
    rem= n%10

    if(rem==0):
        rem=1

    num=num*10 + rem
    n=n//10

rev=0
while(num>0):
    d=num%10
    rev=rev*10+d
    num=num//10

print(rev)