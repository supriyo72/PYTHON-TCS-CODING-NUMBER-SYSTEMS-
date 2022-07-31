n= int(input("Enter a number: "))

def function(n):
    product = 1
    for i in range(1,n+1):
        product= product * i
    return product

a= function(n)
print(a)
