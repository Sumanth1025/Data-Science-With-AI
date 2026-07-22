#assignment operators
# x = 5
# x += 3  # equivalent to x = x + 3
# x -= 2  # equivalent to x = x - 2
# x *= 4  # equivalent to x = x * 4
# x /= 2  # equivalent to x = x / 2
# x %= 3  # equivalent to x = x % 3
# x **= 2  # equivalent to x = x ** 2
# x //= 2  # equivalent to x = x // 2

num=int(input())
num%=2
if num==0:
    print("even")
else:
    print("odd")

num1=1234
num1%=10
print(num1)

# cheackin < or > operator
num2=10
if num2>5:
    print("num2 is greater than 5")
else:
    print("num2 is less than or equal to 5")

#age check
age=int(input())
if age>=18: 
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")


# Assignment Operators
# =

name= "Venkatesh"
print(name)


# augmented assignment operator
# +=, -=,*=,/=,//=,**=

a=10
a=a+6
print(a)

# Tracking number of steps walked in a day 
steps=0
steps+=300
steps+=200
steps+=500
print(steps)

# Argument assignment 
# Deducting bank balance after every transaction

bankBalance=50000
bankBalance-=10000
bankBalance-=5000
bankBalance-=2000
print(bankBalance)

# Argument assignment for multiplication
val1=10
val1*=5
print(val1)

#Doubling the salary of an employee
Salary=50000
Salary*=2
print(Salary)

# Splitting a Bill among 4 members

Bill =5740
Bill/=4
print(Bill)

# Distributing 478 pens to 12 numbers
pens=478
pens//=12
print(pens)


# Checking wheather a number is even or odd 
num = 10
num%=2
print(num)

# Getting last Digit in a number 

num1 = 123
num1 %=10
print(num1)

# Calculate area of a square 

Side=10
Side**=2
print(Side)

# COMPARISION OPERATORS
# Equal to ==

employee=input('Enter your role: ')
print(employee=='admin') 

# Checking given password is equal to saved password
savedpass='Raavi@7965'
password=input('Enter your Password: ')
print(password==savedpass)

# not equal to !=
sate=input('Enter a state which is not a capital: ')
print(sate!='TG')

# > it Check whether the first object is greater than the second object or not
# Checking a person age is a grater than or not
age=int(input('Enter your age: '))
print(age>21)

# Task: write 2 real time examples on each of, >= and <= operators