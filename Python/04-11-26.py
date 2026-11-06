# class Navigation:
#     def navigate(self):
#         print('Finding the default possible rout')
# class Car(Navigation):
#     def navigate(self):
#         print('Finding the best rout for four wheeler')
# class Bike(Navigation):
#     def navigate(self):
#         print('Finding the best rout for two wheeler')
# navigationapp=Navigation()
# navigationapp.navigate()
# carNav=Car()
# carNav.navigate()
# bikeNav=Bike()
# bikeNav.navigate()


# class NormalSeason:
#     def __init__(self,shAmt):
#         self.shAmt=shAmt
    
#     def billAfterDis(self):
#         discount=0
#         bill=self.shAmt-(self.shAmt*discount/100)
#         return bill

# class SummerSeason(NormalSeason):
#     def billAfterDis(self):
#         discount=10
#         bill=self.shAmt-(self.shAmt*discount/100)
#         return bill
    
# class FestiveSeason(NormalSeason):
#     def billAfterDis(self):
#         discount=20
#         bill=self.shAmt-(self.shAmt*discount/100)
#         return bill

# customer1=NormalSeason(12000)
# print(customer1.billAfterDis())

# customer2=SummerSeason(15000)
# print(customer2.billAfterDis())

# customer3=FestiveSeason(25000)
# print(customer3.billAfterDis())



# class Duck:
#     def sound(self):
#         return 'Duck Quacks'
#     def walk(self):
#         return 'It walks'

# class Horse:
#     def sound(self):
#         return 'It Neighs'
#     def walk(self):
#         return 'It runs'

# class Lion:
#     def sound(self):
#         return 'It roars'
#     def walk(self):
#         return 'It walks without making any sound'

# duck1=Duck()

# horse1=Horse()

# lion1=Lion()

# objs=[duck1,horse1,lion1]

# def verification():
#     for obj in objs:
#         if obj.sound() and obj.walk():
#             print('It is a duck')
# verification()



# class cash:
#     def payment(self):
#         return 'pay by cash'
# class upi:
#     def payment(self):
#         return 'pay by upi'
# class paypal:
#     def payment(self):
#         return 'pay by paypal'
# class card:
#     def payment(self):
#         return 'pay by credit card'
# cash1=cash()
# upi1=upi()
# paypal1=paypal()
# card1=card()

# obj1=[cash1,upi1,paypal1,card1]

# def verifaction():
#     for obj in obj1:
#         if obj.payment():
#             print('It is accepted payment method')
#         else:
#             print('It is not a accepted method')
# verifaction()