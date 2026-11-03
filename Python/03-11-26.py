# #Hierarchical Inheritance

# class Emp:
#     def  logIn(self):
#         print('Enter the office with a timestamp')
#     def logOut(self):
#         print('Leaves the office with the timestamp')

# class Trainer(Emp):
#     def takesclasses(self):
#         print('Takes classes to student')
#     def taskAssiging(self):
#         print('Gives tasks to the students')

# class ProgramerManager(Emp):
#     def dashboardwork(self):
#         print('Uploads tasks and recordings in dashboard')
#     def attendence(self):
#         print('Takes attendance of students')
#     def seminars(self):
#         print('conducts seminars to students')
#     def mocks(self):
#         print('Takes mocks of syudents')

# trainer1=Trainer()
# trainer1.logIn()
# trainer1.takesclasses()
# trainer1.taskAssiging()
# trainer1.logOut()

# print('-'*50)

# pm1=ProgramerManager()
# pm1.logIn()
# pm1.dashboardwork()
# pm1.attendence()
# pm1.mocks()
# pm1.logOut()



# class Vehivle:
#     def __init__(self,fuelcap):
#         self.fuelcap=fuelcap
#         self.fuel=0
#     def refuel(self,amount):
#         if self.fuel+amount <= self.fuelcap:
#             self.fuel+=amount
#             return self.fuel
#         else:
#             return 'Fuel capacity exceeded'
# class Car(Vehivle):
#     def drive(self,km):
#         fuelNeed=km*1.0
#         if self.fuel>=fuelNeed:
#             self.fuel-=fuelNeed
#             return self.fuel
#         else:
#             return 'Not enough fuel to drive'
# class Bike(Vehivle):
#     def ride(self,km):
#         fuelNeeded=km*0.5
#         if self.fuel>=fuelNeeded:
#             self.fuel-=fuelNeeded
#             return self.fuel
#         else:
#             return 'Not enough fuel to drive'
# car1=Car(50)
# print(car1.refuel(30))
# print(car1.drive(25))
# print(car1.refuel(10))
# print(car1.drive(10))

# print('-'*50)

# bike1=Bike(30)
# print(bike1.refuel(30))
# print(bike1.ride(60))
# print(bike1.refuel(20))
# print(bike1.ride(10))




def reverse_odd(s):
    result=""
    odd=""
    i=0
    while i<len(s):
        if i%2!= 0:
            odd=s[i]+odd
        else:
            result+=s[i]
        i+=1
    final=""
    i=0
    j=0
    while i<len(s):
        if i%2==0:
            final+=s[i]
        else:
            final+=odd[j]
            j+=1
        i+=1
    return final
s = input("Enter a string: ")
print(reverse_odd(s))




def reverse_odd(s):
    result=""
    odd=""
    i=0
    while i<len(s):
        if i%2!=0:
            odd=s[i]+odd
        else:
            result+=s[i]
        i+=1
    final=""
    j=0
    i=0
    for ch in s:
        if i%2==0:
            final+=ch
        else:
            final+=odd[j]
            j+=1
        i+=1
    return final
s=input("Enter a string: ")
print(reverse_odd(s))




def reverse_odd(s):
    odd=""
    result=""
    i=0
    while i<len(s):
        if i%2!=0:
            odd=s[i]+odd
        i+=1
    return "".join(s[i] if i%2==0 else odd[i//2] for i in range(len(s)))
s=input("Enter a string: ")
print(reverse_odd(s))