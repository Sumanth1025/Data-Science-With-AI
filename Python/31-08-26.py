# def add():
#     num1=int(input())
#     num2=int(input())
#     print(num1+num2)
# add()


#write a function to check a number is even or odd
# def even_or_odd():
#     if n%2==0:
#         return(f"{n} is Even")
#     else:
#         return(f"{n} is Odd")
# n=int(input('Enter a number:'))
# print(even_or_odd())

# def Odd_numbers():
#     for i in range(1,51):
#         if i%2!=0:
#             print(i)
# Odd_numbers()

# def is_prime():
#     if n < 2:
#         print('Not a prime number')
#         return
#     i = 2
#     while i < n:
#         if n % i == 0:
#             print('Not a prime number')
#             return
#         i += 1
#     print('Prime number')
# n = int(input('Enter the number: '))
# is_prime()


# def is_prime():
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         print(f'The number {n} is prime')
#     else:
#         print(f'The number {n} not is prime')
# n=int(input("Enter the number"))
# is_prime()




#write a function program to print factorial of a number
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=int(input("Enter the number: "))
# print(f"The factorial of {n} is {factorial(n)}")


#or

# def factorial(n):
#     temp=1
#     while n >=1:
#         temp*=n
#         n-=1
#     return temp
# n=int(input("Enter the number"))
# print(f"The factorial of {n} is {factorial(n)}")




#write a function to give discount to customer such that if customer makes a bill greater than 10000 give 10% discount if bill is greater then 5000 give 5% discount
#else 2% discount
# def discount():
#     if n > 10000:
#         discount_amount = n * 0.10
#     elif n > 5000:
#         discount_amount = n * 0.05
#     else:
#         discount_amount = n * 0.02
#     final_amount = n - discount_amount
#     print(f"The final amount after discount is: {final_amount}")
# n = float(input("Enter the bill amount: "))
# discount()