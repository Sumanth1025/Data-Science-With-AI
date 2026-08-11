
a, b = map(int, input("Enter two integers: ").split())
if b != 0:
    print(a / b)
else:
    print("Cannot Divide")




used = int(input("Enter used space (GB): "))
if used < 64:
    print("Space Available")
else:
    print("Storage Full")



delay = int(input("Enter delay in minutes: "))
if delay > 10:
    print("Late")
else:
    print("On Time")



battery = int(input("Enter battery percentage: "))
if battery < 20:
    rint("Power Saving Mode")
else:
    print("Normal Mode")



bill = int(input("Enter bill amount: "))
if bill >= 999:
    print("Free Delivery")
else:
    print("Delivery Charges Apply")



a = 10
b = 2.5
c = 'Hi'
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))



a = 100
b = a
print(id(a), id(b))
print("Same id values" if id(a) == id(b) else "Different id values")



x = 'Hi'
y = 'Hi'
print(id(x), id(y))
print("Same Address" if id(x) == id(y) else "Different Address")



a, b = 10, 2
result = a / b
print(result, type(result))



a, b = 2, 5
result = a ** b
print(result, type(result))



username = input("Enter username: ")
if len(username) >= 8:
    print("Valid Username")
else:
    print("Invalid Username")



roll = input("Enter roll number: ")
if len(roll) == 10:
    print("Valid")
else:
    print("Invalid")



code = input("Enter product code: ")
if len(code) >= 6:
    print("Accepted")
else:
    print("Rejected")



pwd = input("Enter password: ")
if len(pwd) >= 12:
    print("Strong Password")
else:
    print("Weak Password")




team = list(map(int, input("Enter member IDs separated by space: ").split()))
if len(team) >= 11:
    print("Complete Team")
else:
    print("Incomplete Team")




s = input("Enter a string: ")
print(s[0], s[-1])




s = input("Enter an odd-length string: ")
print(s[len(s) // 2])



s = input("Enter a string: ")
if s[0] == s[-1]:
    print("Palindrome Ends")
else:
    print("Not Palindrome Ends")




lst = list(map(int, input("Enter comma-separated numbers: ").split(',')))
print(lst[2])




t = tuple(map(int, input("Enter comma-separated numbers: ").split(',')))
print(t[-1])




emp = input("Enter employee ID: ")
print(emp[::-1])




dept = input("Enter department code: ")
print(dept[:4])




num = input("Enter number/string: ")
print(num[-4:])



s = input("Enter an even-length string: ")
print(s[:len(s) // 2])



code = input("Enter secret code: ")
if code[:3] == "ABC":
    print("Verified")
else:
    print("Rejected")

