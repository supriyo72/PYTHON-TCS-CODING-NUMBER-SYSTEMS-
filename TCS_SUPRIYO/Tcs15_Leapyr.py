year= int(input("Enter a year: "))

def leapYear(year):
    if(year%400 == 0 or year%4 ==0 and year%100 != 0):
        print("leap year")
    else:
        print('Not leap year')


a= leapYear(year)
print(a)