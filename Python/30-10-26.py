# class Animal:
#     def eat(self):
#         print('This animal eats food')
#     def sleep(self):
#         print('This animal sleeps')
# class lion(Animal):
#     def __init__(self,name):
#         self.name=name
#     def sound(self):
#         print('Lion Roars')
#     def hunts(self):
#         print('Lion hunts for its food')
# lion1=lion('Balayya')
# print(lion1.name)
# lion1.eat()
# lion1.hunts()



# class mobilephone():
#     def call(self):
#         print('Calling a number')
#     def message(self):
#         print('Message sent to a number')
# class smartphone(mobilephone):
#     def socialmedia(self):
#         print('Running Instagram')
#     def videocalls(self):
#         print('calling ..friend')
# mobile1=mobilephone()
# mobile1.call()

# smartphone1=smartphone()
# smartphone1.call()
# smartphone1.videocalls()



class BankAccount:
    def __init__(self,name,accno,balance):
        self.name=name
        self.accno=accno
        self.balance=balance
    def deposit(self,amount):
        if amount>1000:
            self.balance+=amount
        else:
            print('Invalid Amount')
class SavingAccount(BankAccount):
    def __init__(self,name,accno,balance):
        super().__init__(name, accno, balance)
        self.intrest=0.05
saving1=SavingAccount('venkat',5646785678,70)
print(saving1.name)