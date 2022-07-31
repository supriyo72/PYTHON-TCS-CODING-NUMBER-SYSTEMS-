r= int(input("The range you want: "))
n1= int(input('Enter a 1st no: '))
n2= int(input('Enter a 2nd no: '))


print(n1,end=" ")
print(n2,end=" ")

for i in range(1,r):
    sum= n1+n2
    print(sum,end=" ")
    n1=n2
    n2=sum
