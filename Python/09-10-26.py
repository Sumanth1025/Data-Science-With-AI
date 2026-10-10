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




# def numdigit(num):
#     if num==0:
#         return num
#     return 1+numdigit(num//10)
# print(numdigit(1234))




# def sumofdigit(num):
#     if num==0:
#         return num
#     return num%10 + sumofdigit(num//10)
# print(sumofdigit(121))




# def proDigi(num):
#     if num==0:
#         return 1
#     return num%10 * proDigi(num//10)
# print(proDigi(23))




nested=[1,[2,3],[4,[5,6]]]
def nest(seq):
    for i in seq:
        if type(i)==nested:
            nested(i)
        else:
            print(i)
nest(nested)