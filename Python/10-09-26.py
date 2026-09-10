# #write a program to convert a character from uppercase to lowercase 

# char=input('Enter character:')
# lower=chr(ord(char)+32)
# print(lower)


# char=input('Enter character:')
# upper=chr(ord(char)-32)
# print(upper)


# def lowercase(char):
#     if 'a' <= char <= 'z':
#         upper = chr(ord(char) - 32)
#         print(upper)
#     else:
#         print(f'cannot convert {char} into uppercase')

# lowercase('k')



#write a function to swapcase of each charater in a string
# def swapcase(s):
#     result = ""
#     for char in s:
#         if 'a' <= char <= 'z':
#             result += chr(ord(char) - 32)
#         elif 'A' <= char <= 'Z':
#             result += chr(ord(char) + 32)
#         else:
#             result += char
#     print(result)
# swapcase("Hello World")



#enumerate

#write a program to assined empids to each and every employee of a company in a function
# def assign_empids(employees):
#     emp_dict = {}
#     for index, employee in enumerate(employees, start=1):
#         emp_dict[employee] = f"EMP{index:03d}" 
#     return emp_dict
# employees = ["Sumanth", "Rahul", "Uma", "Venkat"]
# result = assign_empids(employees)
# print(result)


# def empid(names):
#     companyId = 'VUSA'
#     for empid, name in enumerate(names, start=1):
#         print(f'The employee {name} got empId: {companyId}{empid:03d}')
# empid(['Sumanth', 'Ravi', 'Kiran', 'Uma'])



#take additional list for cities and zip it along with name and sales
emp=['uma','rajesh','sumanth','teja','venkat','janhvi']
sales=[67000,56000,34000,87000,66000,98000]
cities=['Hyderabad','Bheemavaram','Inkollu','mumbai','delhi','bengaluru']
for name,salary,cities in zip(emp,sales,cities):
    print(f'The employee {name} is earning a salary of {salary} and he is from {cities}')