# #1
# name = input("Employee Name: ")
# year = input("Joining Year: ")
# s = ""
# for ch in name:
#     if ch != " ":
#         s += ch
# emp_id = ""
# for i in range(3):
#     emp_id += s[i]
# for i in range(len(s) - 2, len(s)):
#     emp_id += s[i]
# for i in range(len(year) - 2, len(year)):
#     emp_id += year[i]
# print("Generated ID:", emp_id)


# #or


# name = input("Employee Name: ")
# year = input("Joining Year: ")

# name = name.replace(" ", "")
# emp_id = name[:3] + name[-2:] + year[-2:]

# print("Generated ID:", emp_id)




# #2
# score = int(input("Score: "))

# if 90 <= score <= 100:
#     print("Premium")
# elif 75 <= score <= 89:
#     print("Standard")
# elif 50 <= score <= 74:
#     print("Economy")
# elif 0 <= score < 50:
#     print("Reject")
# else:
#     print("Invalid")


# #3
# a = input("Username: ")
# if len(a) >= 8:
#     if a[0].isalpha():
#         if a[-1].isdigit():
#             print("Strong Username")
#         else:
#             print("Weak Username")
#     else:
#         print("Weak Username")
# else:
#     print("Weak Username")


# #4
# s = input("Enter a string: ")

# result = ""

# for i in range(len(s) - 1, -1, -1):
#     if i % 2 == 0:
#         result += s[i]

# print(result)



# #5
# bill = float(input("Bill Amount: "))
# ctype = input("Connection Type: ")
# discount = 0
# if ctype.lower() == "residential":
#     if bill >= 10000:
#         discount = 15
#     else:
#         discount = 10
# elif ctype.lower() == "commercial":
#     if bill >= 10000:
#         discount = 10
#     else:
#         discount = 5
# payable = bill - (bill * discount / 100)
# print("Payable Amount:", payable)




# #6
# sentence = input("Sentence: ")
# word = input("Word: ")
# found = False
# for i in range(len(sentence) - len(word) + 1):
#     if sentence[i:i + len(word)] == word:
#         found = True
#         break
# if found:
#     print("Found")
# else:
#     print("Not Found")






# #7
# password = input("Password: ")
# score = 0
# for ch in password:
#     if 'A' <= ch <= 'Z':
#         score += 2
#     elif 'a' <= ch <= 'z':
#         score += 1
#     elif '0' <= ch <= '9':
#         score += 3
#     else:
#         score += 5
# if score >= 20:
#     print("Score:", score, "Strong")
# elif score >= 10:
#     print("Score:", score, "Medium")
# else:
#     print("Score:", score, "Weak")




# #8
# age = int(input("Age: "))
# membership = input("Membership (Gold/Silver): ")
# borrowed = int(input("Borrowed Books: "))
# if age >= 18:
#     if membership.lower() == "gold":
#         if borrowed < 5:
#             print("Can Borrow")
#         else:
#             print("Cannot Borrow")
#     elif membership.lower() == "silver":
#         if borrowed < 3:
#             print("Can Borrow")
#         else:
#             print("Cannot Borrow")
#     else:
#         print("Invalid Membership")
# else:
#     print("Not Eligible")





# #9
# num = input("Enter Number: ")
# result = ""
# for i in range(len(num)):
#     digit = int(num[i])
#     if i % 2 == 0:
#         result += str(digit * digit)
#     else:
#         result += str(digit * digit * digit)
# print(result)





# #10
# coupon = input("Coupon Code: ")
# purchase = float(input("Purchase Amount: "))
# if coupon.startswith("SALE") and coupon.endswith("2026") and len(coupon) >= 10:
#     print("Coupon Accepted")
#     if purchase >= 5000:
#         print("Discount:30%")
#     else:
#         print("Discount:10%")
# else:
#     print("Invalid Coupon")