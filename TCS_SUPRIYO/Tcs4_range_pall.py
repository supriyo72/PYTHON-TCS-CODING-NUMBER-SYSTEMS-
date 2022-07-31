num1= int(input("Enter a number1: "))
num2= int(input("Enter a number2: "))

for i in range(num1,num2+1):
    rev=0
    num=i
    while(i>0):
        rev= rev*10 + i%10
        i=i//10

    if(rev==num):
        print(num,end=" ")
