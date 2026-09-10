#write a program to define the product name in outer function and product id in inner function and access both the variables
# def outer():
#     productName="HP Laptop"
#     def inner():
#         productId="HP101"
#         return f'The productId of {productName} is {productId}'
#     print(inner())
# outer()




#write a nested function and define an enclosing variable your college name and define a local variable your stream of btech and access both in local scope
# def college():
#     College_name='Vel Tech Rangarajan Dr. Sagunthala R&D Institute of Science and Technology'
#     def Student_Stream():
#         nonlocal College_name
#         College_name='Multi Tech'
#         Stream='Computer Science Engineering'
#         return f'My college name was {College_name} and my stream was {Stream}.'
#     print(Student_Stream())
# college()




#write a nested function to generate emailid for employees for specific domain, pass domain name as parameter for outer function and pass emp id as parameter for inner function and generate the email id inside the inner function.
# def generateEmail(domain):
#     def email(empName):
#         return f'{empName}@{domain}'
#     return email
# domain = generateEmail('microsoft.com')
# empName = domain('uma')
# print('EmailId:',empName)




#
# def banking():
#     balance=20000
#     def withdraw(amount):
#         nonlocal balance
#         if balance >=amount:
#             balance-=amount
#             print('withdraw Succesfull')
#             print(f'Current balance: {balance}')
#     return withdraw
# atm=banking()
# atm(2000)