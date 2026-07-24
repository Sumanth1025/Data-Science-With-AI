#logical operators
#and
age = 20
citizenship = "USA"
print(age >= 18 and citizenship == "Indian")  # True, both conditions are true

#or
age = 16
citizenship = "Indian"
print(age >= 18 or citizenship == "Indian")  # True, one condition is true

#not
age = 20
print(not age < 18)  # True, negates the condition

#cheaking wheather it is an holiday or not
#weekend or public holiday or festival
weekend = False
public_holiday = False
festival = True
print(weekend or public_holiday or festival)  # True, one condition is true

#payment methods
card = 'No'
cash = 'No'
upi = 'Yes'
print(card =='Yes' or cash =='Yes' or upi =='Yes')  # True, one condition is true



#Identity operators
#is
num1 = 10
num2 = 20
print(num1 is num2)  # False, num1 and num2 are not the same object


Chinnodu="sumanth"
student=Chinnodu
print(Chinnodu is student)  # True, Chinnodu and student are the same object


developer = "write code"
tester = "test code"
print(developer is not tester)  # True, developer and tester are not the same object

num1 = 10
print(id(num1))  # True, num1 and 10 are the same object
num2 = 10.0
print(id(num2))
print(num1 is not num2)  # True, num1 and num2 are not the same object


#code optimization: The program create only on object for all variables if the object size is within limits 
# if the size of the object go beyond the limit python create different object for each variable.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)  # False, list1 and list2 are not the same object
print(list1 == list2)  # True, list1 and list2 have the same values

# MEMPERSHIP OPERATOR
#IN
names=['venkatesh','sumanth','uma','abishay','akash']
print('bose' in names)
print('venkatesh'in names)

# NOT IN 
names=['venkatesh','sumanth','uma','abishay','akash']
print('bose' not in names)
print('venkatesh'not in names)