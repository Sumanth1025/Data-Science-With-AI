class School:
    schoolName='Narayana International school'

    def __init__(self,Name,Class,Nickname):
        self.Name=Name
        self.Class=Class
        self.Nickname=Nickname

    def studentDetails(self):
        print(f'Name: {self.Name}')
        print(f'Class: {self.Class}')        
        print(f'Schoolname: {self.schoolName}')
        print(f'Nickname: {self.Nickname}')
        print('-'*80)

student1=School('Obul Reddy','7th','gobbemma')
student2=School('Swapna','6th','muggu')
student3=School('Ajay','6th','gangiraddu')

student1.studentDetails()
student2.studentDetails()
student3.studentDetails()