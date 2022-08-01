A= int(input("Enter a num1: "))
B= int(input("Enter a den1: "))
C= int(input("Enter a num2: "))
D= int(input("Enter a den2: "))

result1= (A*D)+(B*C)
result2= (B*D)

res= result1/result2

print(res)
print("The result= {}/{}".format(result1,result2))