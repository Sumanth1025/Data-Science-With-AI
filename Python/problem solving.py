# #prime number check
# n=int(input("Enter a number: "))
# if n < 2:
#     print("not a prime")
# else:
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             print("not a prime")
#             break
#     else:
#         print("prime")


# #printing next prime number
# n=int(input("Enter a number: "))
# while True:
#     n += 1
#     for i in range(2, int(n**0.5) + 1): 
#         if n % i == 0:
#             break
#     else:
#         print("Next prime number is:", n)
#         break

# #OR
# n=int(input("Enter a number: "))
# b=n+1
# while True:
#     p=True
#     if b<2:
#         p=False
#     else:
#         for i in range(2,int(b**0.5)+1):
#             if b%i==0:
#                 p=False
#                 break
#     if p==True:
#         print("Next prime number is:",b)
#         break


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #Reversing a number
# n=int(input("Enter a number: "))
# rev=0
# while n>0:
#     rev= (rev*10) + n%10
#     n//=10
# print("Reversed number is:",rev)




# #OR
# s=int(input("Enter a number: "))
# s=str(s)
# s=s[::-1]
# s=int(s)
# print("Reversed number is:",s)




# #for character
# s = input("Enter a character: ")
# s=s[::-1]
# print("Reversed character is:",s)




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Armostrong number
n=int(input("Enter a number: "))
a=len(str(n))
sum=0
while n>0:
    r=n%10
    sum+=r**a
    n//=10
print("Sum of digits raised to the power of number of digits is:",sum)
if sum==n:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")



#Neon number
n=int(input("Enter a number: "))
a=n**2
sum=0
while a>0:
    r=a%10
    sum+=r
    a//=10
print("Sum of digits of square is:",sum)
if sum==n:
    print("The number is a Neon number")
else:
    print("The number is not a Neon number")