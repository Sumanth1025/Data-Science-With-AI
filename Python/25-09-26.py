# nums = [1, 2, 4, 8, 16]
# target = 13
# nums.sort()
# closest = nums[0] + nums[1] + nums[2]
# for i in range(len(nums) - 2):
#     left = i + 1
#     right = len(nums) - 1
#     while left < right:
#         total = nums[i] + nums[left] + nums[right]
#         if abs(total - target) < abs(closest - target):
#             closest = total
#         if total < target:
#             left += 1
#         elif total > target:
#             right -= 1
#         else:
#             closest = total
#             break
# print(closest)




#write a code to generate a list of squares of eace values in a list
# def squares(s):
#     return [x**2 for x in s]
# s = list(map(int, input("Enter numbers: ").split()))
# print(squares(s))



# import ast
# def squares(s):
#     return [x**2 for x in s]
# s = ast.literal_eval(input("Enter list: "))
# print(squares(s))



# s = list(map(int, input("Enter numbers: ").split()))
# sq=[]
# for num in s:
#     sq+=[num*num]
# print(sq)


# #using Comprehensions:
# sq=[num*num for num in s]
# print(sq)




# def prime_numbers(s):
#     result = []
#     for n in s:
#         if n > 1:
#             for i in range(2, n):
#                 if n % i == 0:
#                     break
#             else:
#                 result.append(n)
#     return result
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(prime_numbers(s))





# nums=[1,2,3,4,5,6,7,8,9,10]
# evennum=[num for num in nums if num%2==0]
# oddnum=[num for num in nums if num%2!=0]
# print(oddnum)
# print(evennum)



# zeroMatrix=[[0]*3 for i in range(3)]
# print(zeroMatrix)



#names=['kiran','sumanth','shankar','mahesh']
#write a Comprehensions to generate a list of names in upper case we can use upper method.
# names = ['kiran', 'sumanth', 'shankar', 'mahesh']
# upper = [i.upper() for i in names]
# print(upper)



# nums=[56,76,23,11,-2,707,43,90,71,77]
# s=[num for num in nums if num >50 and num < 75]
# print(s)



#generate a list of selling prices by adding 10% of each price to itself using Comprehensions
# costprices = [11299, 13999, 15899, 32999, 56989]
# s = [i + (i * 10 / 100) for i in costprices]
# print(s)



# costprices = [11299, 13999, 15899, 32999, 56989]
# s = [f'{i*1.1:.2f}' for i in costprices]
# print(s)




#write a Comprehensions to genetate a list of username from the emails the part before @ is user name 
# emails=['venkataranayana@spacex.com','sumanthteja@tesla.com','shankar@AI.com','rasagna@asml.com']
# username=[i.split('@')[0] for i in emails]
# print(username)
# domain=[i.split('@')[1] for i in emails]
# print(domain)