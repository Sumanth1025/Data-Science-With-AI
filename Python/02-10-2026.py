# def sumofnum(num1,num2):
#     return num1+num2
# print(sumofnum(4,4))




#one line functions
# print((lambda num1,num2:num1+num2)(4,4))




# print((lambda num1,num2:num1*num2)(4,4))


# print((lambda ba,ex:ba**ex)(5,4))




# print((lambda n1,n2:f'{n1} greatest'if n1>n2 else f'{n2} greatest')(65,75))



# print((lambda n:f'{n} is even' if n%2==0 else f'{n} is odd')(76483))



# print((lambda ba=10,ex=2:ba**ex)())



# print((lambda *nums:sum(nums))(1,3,4,6,8,2))



# print((lambda temp:(temp*1.8)+32)(45))



# print((lambda a, b, c: min(a, b, c))(5, 3, 8))
# print((lambda a, b, c: max(a, b, c))(5, 3, 8))



# print((lambda a,b,c:a if a<b and b<c else b if b<c else c)(5,3,8))



#35
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# result = []
# i = 0
# while i < len(a):
#     found = 0
#     j = 0
#     while j < len(b):
#         if a[i] == b[j]:
#             found = 1
#         j = j + 1
#     if found == 1:
#         already = 0
#         j = 0
#         while j < len(result):
#             if result[j] == a[i]:
#                 already = 1
#             j = j + 1
#         if already == 0:
#             result = result + [a[i]]
#     i = i + 1
# print(result)