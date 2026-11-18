# total=900
# maxmarks=0
# try:
#     percentage=total/maxmarks*100
#     print(f'Percentage: {percentage}')
# except ZeroDivisionError:
#     print('max marks cannot be zero')



# def agecal(birthyear,currentyear):
#     try:
#         age=currentyear-birthyear
#         print(age)
#     except TypeError:
#         print('Enter date of birth in  numbers') 
# agecal('Two thousand and five','two thousand twenty six')        
# agecal(2005,2026)



# def prime(n):
#     try:
#         if n<2:
#             print('Not a prime number')
#         else:
#             for i in range(2,n):
#                 if n%i==0:
#                     print('Not a prime number')
#                     break
#             else:
#                 print('Prime number')
#     except TypeError:
#         print('Enter a number in digits')
# prime('five')
# prime(5)



# def prime():
#     try:
#         n=int(input('enter a number: '))
#         count=0
#         for i in range(1,n+1):
#             if n%i==0:
#                 count+=1
#         if count==2:
#             print(f'{n} id prime')
#         else:
#             print(f'{n} is not prime')
#     except ValueError:
#         print('Enter a number in digits')
# prime()