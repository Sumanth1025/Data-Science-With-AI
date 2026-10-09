# import time
# def printnum(num):
#     if num<1:
#         print('Boom')
#         return
#     print(num)
#     time.sleep(1)
#     printnum(num-1)
# printnum(10)




# def AddNum(num):
#     if num==10:
#         return num
#     return num + AddNum(num+1)
# print(AddNum(1))




# def Fact(num):
#     if num==1:
#         return num
#     return num * Fact(num-1)
# print(Fact(5))




def numdigit(num):
    if num==0:
        return num
    return 1+numdigit(num//10)
print(numdigit(1234))