# class School:
#     schoolName='Narayana International school'

#     def __init__(self,Name,Class,Nickname):
#         self.Name=Name
#         self.Class=Class
#         self.Nickname=Nickname

#     def studentDetails(self):
#         print(f'Name: {self.Name}')
#         print(f'Class: {self.Class}')        
#         print(f'Schoolname: {self.schoolName}')
#         print(f'Nickname: {self.Nickname}')
#         print('-'*80)

# student1=School('Obul Reddy','7th','gobbemma')
# student2=School('Swapna','6th','muggu')
# student3=School('Ajay','6th','gangiraddu')

# student1.studentDetails()
# student2.studentDetails()
# student3.studentDetails()





class Bank:
    bankName = 'SBI'

    def __init__(self, Name, PhoneNumber, MinimumBalance, Branch):
        self.Name = Name
        self.PhoneNumber = PhoneNumber
        self.MinimumBalance = MinimumBalance
        self.Branch = Branch

    def customerDetails(self):
        print(f'Customer Name: {self.Name}')
        print(f'Phone Number: {self.PhoneNumber}')
        print(f'Minimum Balance: ₹{self.MinimumBalance}')
        print(f'Branch Name: {self.Branch}')
        print(f'Bank Name: {self.bankName}')
        print('-' * 80)


customer1 = Bank('Obul Reddy', '9876543210', 1000, 'Hyderabad')
customer2 = Bank('Swapna', '9876543211', 2000, 'Vijayawada')
customer3 = Bank('Ajay', '9876543212', 1500, 'Chennai')


customer1.customerDetails()
customer2.customerDetails()
customer3.customerDetails()