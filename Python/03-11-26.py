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




# class SmartDevice:
#     def Poweron(self):
#         print("Power on the device")

#     def Poweroff(self):
#         print("Device is turned off")


# class SmartSecSystem(SmartDevice):
#     def IntructionDetecton(self):
#         print("Detects the instruction give ")

#     def alarm(self):
#         print("Ring the Alarm!!!")

# class SamartAssistant(SmartDevice):
#     def playMusic(self):
#         print("playing Music")

#     def vioceBrowsing(self):
#         print("Searching for the answer to your question ")
#         print("Answering your qurryg.....")


# class RemoteControl(SmartSecSystem,SamartAssistant ):
#     pass

# remote1=RemoteControl()
# remote1.Poweron()
# remote1.IntructionDetecton()
# remote1.alarm()
# remote1.playMusic()
# remote1.vioceBrowsing()



class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def displayPerson(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):
    def __init__(self,name,age,scholarship,total_fees):
        super().__init__(name,age)
        self.scholarship=scholarship
        self.total_fees=total_fees

    def displayStudent(self):
        self.displayPerson()
        print("Total Fees:",self.total_fees)
        print("Scholarship:",self.scholarship)
        print("Remaining Fees:",self.total_fees -self.scholarship)

class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary

    def displayEmployee(self):
        self.displayPerson()
        print("Salary:",self.salary)

class PHDStudent(Student,Employee):
    def __init__(self,name,age,scholarship,salary,total_fees):
        Person.__init__(self,name,age)
        self.scholarship=scholarship
        self.salary=salary
        self.total_fees=total_fees

    def displayPHDStudent(self):
        self.displayPerson()
        print("Total Fees:",self.total_fees)
        print("Scholarship:",self.scholarship)
        print("Remaining Fees:",self.total_fees - self.scholarship)
        print("Salary:",self.salary)


s1 = Student("Rahul",21,25000,100000)
s1.displayStudent()
print("-"*50)
e1 = Employee("Kiran",25,50000)
e1.displayEmployee()
print("-"*50)
p1 = PHDStudent("Sumanth",24,40000,30000,120000)
p1.displayPHDStudent()