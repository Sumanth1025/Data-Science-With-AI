#Type Conversion
#Type conversion and type casting in python
#Type conversion is the process of converting one data type to another data type
#Type casting is the process of converting one data type to another data type explicitly by the user
#Type conversion is done by python automatically but type casting is done by the user explicitly
#Type conversion is also called implicit type conversion and type casting is also called explicit type conversion
#Type conversion is done by python automatically when we perform operations between different data types

#operation between int and float is possible in python
num1=10#int
num2=12.5#float
total=num1+num2#float

#auto type conversion of data types done by python iss called
#type conversion
print("Total:", total)

#operation between int and bool is possible in python
bool1=True #by default True is considered as 1
num=12
total=bool1+num #1+12=13
print("Total:", total)

bool2=False #by default False is considered as 0
num=10
total=bool2+num #0+10=10
print("Total:", total)

#operation between float and bool is possible in python
#str1="10" #string
#num=10 #int
#total=str1+num #concatenation of string and int
#print("Total:", total)                               #gives error because we cannot concatenate string and int in python

str1="10" #string
num=10 #int
total=str1+str(num) #concatenation of string and int
print("Total:", total)

#operation between string and string is possible in python
str1="s"
str2="u"
print("Total:", str1+str2) #concatenation of strings

#operation between complex number and int is possible in python
com1=3+4j #complex number
num1=10 #int
total=com1+num1 #complex number + int = complex number
print("Total:", total)

#operation between complex number and float is possible in python
com1=3+4j #complex number
num1=12.5 #float
total=com1+num1 #complex number + float = complex number
print("Total:", total)

#operation between complex number and complex number is possible in python
imgCom2=5j #complex number
Com1=22+20j #complex number
total=imgCom2+Com1 #complex number + complex number = complex number
print("Total:", total)

#Type casting
#Type casting is done by the user explicitly when we want to convert one data type to another data type
#Type casting is done by using the built-in functions like int(), float(), str(), complex(), bool() etc.
#Type casting is also called explicit type conversion
#Type casting is done by using the built-in functions like int(), float(), str(), complex(), bool() etc.

#operation between int and float is possible in python
salary=10000 #int
print(float(salary)) #float

#operation between float and int is possible in python
num=12.5 #float
print(int(num)) #int

#operation between int and complex number is possible in python
# com1=3+4j #complex number
# print(int(com1)) #int                     #gives error because we cannot convert complex number to int in python

#operation between int and complex number is possible in python
int1=10 #int
print(complex(int1)) #complex

#operation between int and string is possible in python
price=1000 #int
print(str(price)) #str
print(type(str(price))) #str

#operation between list and tuple is possible in python
list1=[1,2,3,4,5] #list
# print(tuple(list1)) #tuple
print(set(list1)) #set

#operation between tuple and list is possible in python
tuple1=(1,2,3,4,5) #tuple
print(list(tuple1)) #list

#Operation between int and dict is possible in python
# num1 = 10 #int
# print(dict(num1))                      #gives error because we cannot convert int to dict in python



#range
# list1=list(range(1,11)) #list
# print(list1) #list

print(list(range(1,11,2))) #list

#it will take as a end and start the value from 0
#print(list(range(10))) #list

#negative range 
print(list(range(20,0,-10))) #list


#len():It return the number of items in the sequence. It can be used with strings, lists, tuples, sets, and dictionaries.
# str1="Hello, World!"
# print(len(str1)) #13

# list1=[1,2,3,4,5]
# print(len(list1)) #5

# tuple1=(1,2,3,4,5)
# print(len(tuple1)) #5

# set1={1,2,3,4,5}
# print(len(set1)) #5

# dict1={"a":"venk","b":2,"c":3}
# print(len(dict1)) #3

