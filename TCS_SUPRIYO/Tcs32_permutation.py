# Input: N = 5, r = 3
# Output: 60
# Explanation: To permute n people in r seats we have to find the value of n!/(n-r)!.The value of 5!/(5-3)! Is 60.

n= int(input("Enter n: "))
r= int(input("Enter r: "))

a=n-r
product=1
for i in range(1,n+1):
    product=product*i

permutaion= product/a
print(permutaion)
