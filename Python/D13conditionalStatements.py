# #write a program to check wheather a number is even or odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(num, "is an even number.")
# else:
#     print(num, "is an odd number.")



# password = input("Enter your password: ")
# if len(password) >= 8:
#     print("Password has enough characters.")
# else:
#     print("Password is too short. It must be at least 8 characters long.")


# #write a program to withdraw money from my account
# withdrawal = float(input("Enter the amount to withdraw: "))
# balance = 10000.0  # Example account balance
# if withdrawal <= balance:
#     balance -= withdrawal
#     print("Withdrawal successful. New balance is:", balance)
# else:
#     print("Insufficient funds. Your balance is:", balance)

#write a program to check wheather a person login or not
# password = input("Enter your password: ")
# saved_password = "sumanth"
# if password == saved_password:
#     print("Login successful.")
# else:
#     print("Login failed. Incorrect password.")

#write a program to check wheather a person is eligible for loan or not bassed on his salary
# salary = float(input("Enter your salary: "))
# if salary >= 50000:
#     print("You are eligible for a loan.")
# else:
#     print("You are not eligible for a loan.")


# write a program to check wheather an employee can login or not
# emp_ids = [101,102,103,104]
# fingerprint = input("Enter wheather the fingerprint is valid or not: ")
# emp_id = int(input("Enter your employee ID: "))
# if emp_id in emp_ids and fingerprint == "valid":
#     print("Employee login successful.")
# else:
#     print("Employee login failed. Please check your credentials.") 


#write a program to check wheather a person is eligible for loan or not bassed on his salary and cibil schore
# salary = float(input("Enter your salary: "))
# cibil_score = int(input("Enter your CIBIL score: "))
# if salary >= 50000 and cibil_score >= 750:
#     print("You are eligible for a loan.")
# else:
#     print("You are not eligible for a loan.")


#or operator
#write a program to check wheather a student has requires qualification to apllpy for a jod
graduation = input("Enter your qualification: ")
if graduation == "degree" or graduation == "B.Tech":
    print("You are eligible to apply for the job.")
else:
    print("You are not eligible to apply for the job.")