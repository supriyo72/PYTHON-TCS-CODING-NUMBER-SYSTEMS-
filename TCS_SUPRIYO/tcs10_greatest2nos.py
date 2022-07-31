num1= int(input("Enter 1st no: "))
num2= int(input("Enter 2nd no: "))
num3= int(input("Enter 3rd no: "))

def function(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num3 and num2>num1):
        return num2
    else:
        return num3
    
a= function(num1,num2,num3)
print("greatest number is: ",a)
