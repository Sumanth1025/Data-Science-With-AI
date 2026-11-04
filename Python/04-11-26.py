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



class Duck:
    def sound(self):
        retuen 'Duck Quacks'
    def walk(self):
        print('It walks')

class Horse:
    def sound(self):
        print('It Neighs')
    def walk(self):
        print('It runs')

class Lion:
    def sound(self):
        print('It roars')
    def walk(self):
        print('It walks without making any sound')

duck1=Duck()

horse1=Horse()

lion1=Lion()

objs=[duck1,horse1,lion1]

def verification():
    for obj in objs:
        if obj.sound() and obj.walk():
            print(f'{obj} is a duck')
verification()