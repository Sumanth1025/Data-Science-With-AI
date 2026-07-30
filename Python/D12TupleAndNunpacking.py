#packing
import string


num1=10,20,30
print(num1)

#unapcking
num2=10,20,30
a,b,c=num2
print(a)
print(b)
print(c)


#unpacking with variable length
name=["Alice","Bob","Charlie"]
name,*remNames=name
print(name)
print(remNames)


#string concatenation
str1="Hello"
str2="world !"
print(str1+str2)

#string Replication
print("="*30)
print("Uma wed sowmya")
print("Date: 31/07/2026")
print("Venue: Inkollu UHS school")
print("="*30)



# if raining=="yes":
#     print("Thaduchukuntu podham")
# else:
#     print("Thadava kunda podham")

#tickting booking
age=int(input('enter the age:'))
if age>18:
    print('you can buy a ticket')
else:
    print('you cannot buy a ticket')
