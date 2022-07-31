# Example 1:
# Input: 18
# Output: Abundant Number
# Explanation: Divisors of 18 are 1,2,3,6,9. 1+2+3+6+9=21, Since 21 is greater than 18, 18 is an abundant number.
# n= int(input("Enter a num: "))

temp=n
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i    
        
if(sum>temp):
    print("Abundant")
else:
    print("Not Abundant")
    
