n=int(input("Enter a no: "))

def func(n):
    if n==1 or n==0:
          return 1
    else:
          return n* func(n-1)
a= func(n)
print(a)