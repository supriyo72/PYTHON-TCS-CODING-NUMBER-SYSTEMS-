# a= float(input("Enter value of a: "))
# d= float(input("Enter value of d: "))
# n= float(input("Enter value of n: "))

# def apSeries(a,d,n):
#     sum= (n / 2.0) * (2.0 * a + (n - 1) * d);
#     return sum
    
# A= apSeries(a,d,n)
# print(A)






# a= int(input("Enter value of a: "))
# d= int(input("Enter value of d: "))
# n= int(input("Enter value of n: "))

# sum=0
# for i in range(1,n+1):
#     sum=sum+a
#     a= a+d
    
# print(sum)






a= float(input("Enter value of a: "))
d= float(input("Enter value of d: "))
n= float(input("Enter value of n: "))

sum=0
i=1
while(i<=n):
    sum=sum+a
    a= a+d
    i+=1
print(sum)