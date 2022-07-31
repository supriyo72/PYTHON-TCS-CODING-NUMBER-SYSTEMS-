# Example 1:
# Input: 378
# Output: Yes it is a Harshad number.
# Explanation: 3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number.

n=int(input("Enter a number: "))

temp=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
    
if(temp%sum==0):
    print("The no is Harshad")
else:
    print("Not harshad")
