n= int(input("Enter n: "))
k= int(input("Enter k: "))
# n=5 k=3--> 5x5x5=125
prod=1
for i in range(1,k+1):
      prod= prod*n
print(prod)