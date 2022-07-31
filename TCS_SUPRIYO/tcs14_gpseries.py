# a= float(input("Enter value of a: "))
# r= float(input("Enter value of r: "))
# n= float(input("Enter value of n: "))

# def apSeries(a,d,n):
#     sum= (a * r**n -1) / (r - 1);
#     return sum
    
# A= apSeries(a,r,n)
# print(A)






a= float(input("Enter value of a: "))
r= float(input("Enter value of r: "))
n= float(input("Enter value of n: "))

sum=0
i=1
while(i<=n):
    sum=sum+a
    a= a*r
    i+=1
print(sum)
