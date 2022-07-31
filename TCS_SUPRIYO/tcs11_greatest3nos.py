num1= int(input("Enter 1st no: "))
num2= int(input("Enter 2nd no: "))
num3= int(input("Enter 3rd no: "))

def function(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    if(num2>num3):
        return num2
    else:
        return num3
    
a=function(num1,num2,num3)
print("Greatest: ",a)