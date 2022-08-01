n=int(input("Enter a no: "))
temp=n
prod= n*n
a=prod%100

print("The product of "+ str(n) + " is: " + str(prod))

if(a==temp):
    print("Automorphic")
else:
    print("Not Automorphic")
