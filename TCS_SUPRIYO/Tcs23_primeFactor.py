num= int(input("Enter a number: "))

i=2
temp=num
while(temp>1):
    if(temp%i==0):
        print(i, end= " ")
        temp= (temp/i)
    else:
        i=i+1




