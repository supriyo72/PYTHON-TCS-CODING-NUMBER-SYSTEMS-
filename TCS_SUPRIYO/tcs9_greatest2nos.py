num1= int(input("Enter 1st no: "))
num2= int(input("Enter 2nd no: "))

def function(num1,num2):
    if(num1>num2):
        return num1
    else:
        return num2
    
a= function(num1,num2)
print("greatest number is: ",a)
