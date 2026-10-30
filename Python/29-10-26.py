# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def details(self):
#         print(f'Name:{self.name}')
#         print(f'Marks:{self.marks}')
# student1=Student('uma_sowmya',90)
# student1.details()


# class Employee:
#     def __init__(self,empid,name,salary):
#         self.empid=empid
#         self.name=name
#         self._salary=salary
#     def details(self):
#         print(f'EMPID:{self.empid}')
#         print(f'Name:{self.name}')
#         print(f'Salary:{self._salary}')
#     def salaryhike(self,hike):
#         self._salary+=hike

# emp1=Employee(1,'Uma',40000)
# emp1.details()
# emp1.salaryhike(12000)
# print(emp1._salary)



# class Bank:
#     def __init__(self,name,acno,balance):
#         self.name=name
#         self._acno=acno
#         self.__balance=balance
#     def custdetails(self):
#         print(f'CustName:{self.name}')
#         print(f'ACNO:{self._acno}')
#     def checkbal(self):
#         print(f'Balance:{self.__balance}')
# cust1=Bank('Venky',1234567890,1000)
# cust1.custdetails()
# cust1.checkbal()



# class Mobile:
#     def __init__(self,price,quantity):
#         self.price=price
#         self._quantity=quantity
#     def __compro(self):
#         invester=500000000
#         sales=self.price*self._quantity
#         tax=sales*20
#         shares=200000000
#         netpro=invester+sales+tax+shares
#         return netpro
#     def empsalary(self):
#         sal=self.__compro()*0.0001
#         return f'{sal:.2f}'
# salesman1=Mobile(35999,80)
# print(salesman1.empsalary())