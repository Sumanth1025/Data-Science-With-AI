#Mutable/changable and Immutable/non changable
list1=[1,2,3,4,5]
print(list1)
print(id(list1))
list1+=(6,7,8,9,10)
print(list1)
print(id(list1))

#cheaking immutability of int data type
int1=10
print(int1)
print(id(int1))
int1+=10
print(int1)
print(id(int1))

#cheacing immutability of float and complex data types
float1=10.5
print(float1)
print(id(float1))
float1+=10.5
print(float1)
print(id(float1))

complex1=10+5j
print(complex1)
print(id(complex1))
complex1+=5+10j
print(complex1)
print(id(complex1))

#since set and dictinary are unorder we can't use += for that
#we use |=
set1={'uma','suma','kuma','puma'}
print(set1)
print(id(set1))
set1 |= {'ruma'}
print(set1)
print(id(set1))

dict1={'name':'uma','age':20,'place':'kollam'}
print(dict1)
print(id(dict1))
dict1 |= {'gender':'female'}
print(dict1)
print(id(dict1))


# name=input("Enter your name:")
# print(f'Hello {name}, Welcome to python programming')

#by default input function takes string data type, if we want to take integer or float we have to convert it into int or float
num1=input("Enter your number:")
num2=input("Enter your number:")
print(num1+num2)


num1=int(input("Enter your number:"))
num2=float(input("Enter your number:"))
print(num1+num2)

#cheaking Arithmetic operations:
num1=int(input("Enter your number:"))
num2=int(input("Enter your number:"))
print(f'Addition of {num1} and {num2} is {num1+num2}')
print(f'Subtraction of {num1} and {num2} is {num1-num2}')
print(f'Multiplication of {num1} and {num2} is {num1*num2}')
print(f'Division of {num1} and {num2} is {num1/num2}')
print(f'Floor Division of {num1} and {num2} is {num1//num2}')
print(f'Modulus of {num1} and {num2} is {num1%num2}')
print(f'Exponentiation of {num1} and {num2} is {num1**num2}')