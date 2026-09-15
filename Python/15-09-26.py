# problen solving
#1. check whether a number is spy number or not
# def is_spy_number(num):
#     digits = [int(d) for d in str(num)]
#     digit_sum = sum(digits)
#     digit_product = 1
#     for d in digits:
#         digit_product *= d
#     return digit_sum == digit_product
# print(is_spy_number(22))


# def spy_number(num):
#     temp=num
#     sum = 0
#     product = 1
#     while temp > 0:
#         digit = temp % 10
#         sum += digit
#         product *= digit
#         temp //= 10
#     if sum == product:
#         print(f'{num} is a Spy Number')
#     else:
#         print(f'{num} is Not a Spy Number')
# num = int(input("Enter a number: "))
# spy_number(num)




# def spy_number(num):
#     temp = num
#     sum = 0
#     product = 1
#     while temp > 0:
#         digit = temp % 10
#         sum += digit
#         product *= digit
#         temp //= 10
#     if sum == product:
#         return True
#     else:
#         return False
# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
# print("Spy numbers are:")
# for num in range(start, end + 1):
#     if spy_number(num):
#         print(num)



# def spy_number(num):
#     temp = num
#     sum = 0
#     product = 1
#     while temp > 0:
#         digit = temp % 10
#         sum += digit
#         product *= digit
#         temp //= 10
#     if sum == product:
#         return True
#     else:
#         return False
# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
# print("Spy numbers are:")
# while start <= end:
#     if spy_number(start):
#         print(start)
#     start += 1



#write Harshad number
# def HarNum(num):
#     temp=num
#     sum=0
#     while temp>0:
#         digit=temp%10
#         sum+=digit
#         temp//=10
#     if num % sum ==0:
#         print(f'{num} is a Harshad number')
#     else:
#         print(f'{num} is not a Harshad number')
# num=int(input('enter the number'))
# HarNum(num)


# def HarNum(num):
#     temp=num
#     sum=0
#     while temp>0:
#         digit=temp%10
#         sum+=digit
#         temp//=10
#     if num % sum ==0:
#         return True
#     else:
#         return False
# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
# print("Spy numbers are:")
# while start <= end:
#     if HarNum(start):
#         print(start)
#     start += 1



#Armstrong number
# def ArmNum(num):
#     temp=num
#     sum=0
#     l=len(str(num))
#     while temp>0:
#         digit=temp%10
#         sum+=digit**l
#         temp//=10
#     if num == sum:
#         print(f'{num} is an Armstrong number')
#     else:
#         print(f'{num} is not an Armstrong number')
# num=int(input('enter the number'))
# ArmNum(num)



# def ArmNum(num):
#     temp=num
#     count=0
#     while temp>0:
#         temp//=10
#         count+=1
#     temp1=num
#     sum=0
#     while temp1 >0:
#         digit=temp1%10
#         sum+=digit**count
#         temp1//=10
#     if num == sum:
#         print(f'{num} is an Armstrong number')
#     else:
#         print(f'{num} is not an Armstrong number')
# num=int(input('enter the number'))
# ArmNum(num)



# def ArmNum(num):
#     temp=num
#     count=0
#     while temp>0:
#         temp//=10
#         count+=1
#     temp1=num
#     sum=0
#     while temp1 >0:
#         digit=temp1%10
#         sum+=digit**count
#         temp1//=10
#     if num == sum:
#         return True
#     else:
#         return False
# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
# print("Spy numbers are:")
# while start <= end:
#     if ArmNum(start):
#         print(start)
#     start += 1




# def ArmNum(num):
#     temp = num
#     count = 0
#     while temp > 0:
#         temp //= 10
#         count += 1
#     temp1 = num
#     sum = 0
#     while temp1 > 0:
#         digit = temp1 % 10
#         sum += digit ** count
#         temp1 //= 10
#     if num == sum:
#         return True
#     else:
#         return False
# num = 10
# count = 0
# print("First 10 Armstrong numbers are:")
# while count < 10:
#     if ArmNum(num):
#         print(num)
#         count += 1
#     num += 1




# def ArmNum(num):
#     temp = num
#     count = 0
#     while temp > 0:
#         temp //= 10
#         count += 1
#     temp1 = num
#     sum = 0
#     while temp1 > 0:
#         digit = temp1 % 10
#         sum += digit ** count
#         temp1 //= 10
#     if num == sum:
#         return True
#     else:
#         return False
# start = 1
# n = int(input("Enter number"))
# count = 0
# print("First", n, "Armstrong numbers are:")
# while count < n:
#     if start >= 10 and ArmNum(start):
#         print(start)
#         count += 1
#     start += 1




#Automorphic number:
def AuphNum(num):
    temp=num
    square=num**2
    while temp>0:
        digit=temp%10
        if digit != square%10:
            print(f'{num} is not an Automorphic number')
            return
        temp//=10
        square//=10
    print(f'{num} is an Automorphic number')
num=int(input())
AuphNum(num)