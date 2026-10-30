# #Missing number
# def missing(series):
#     n=len(series)+1
#     rangesum=(n*(n+1))//2
#     actualsum=0
#     i=0
#     while i<len(series):
#         actualsum+=series[i]
#         i+=1
#     number=rangesum-actualsum
#     return f'The missing number is: cl{number}'
# list1=[1,2,4,5,6,7,8,9,10]
# print(missing(list1))


# #second largest in list
# def seclar(series):
#     larg=0
#     seclarg=0
#     for num in series:
#         if num>larg:
#             seclarg=larg
#             larg=num
#         elif larg>num>seclarg:
#             seclarg=num
#     return seclarg
# list1=[12,4,7,11,78,45,9]
# print(seclar(list1))




# #rotate first num to last num
# def firsttolast(n):
#     temp=n
#     count=0
#     while temp>0:
#         temp//=10
#         count+=1
#     firdig=n//(10**(count-1))
#     remdig=n%(10**(count-1))
#     rotdig=remdig*10+firdig
#     return rotdig
#     # return f'{remdig}{firdig}'
# print(firsttolast(1234))




# #rotate last num to first num
# def lasttofirst(n):
#     lastdig=n%10
#     remdig=n//10
#     count=0
#     temp=n
#     while temp>0:
#         temp//=10
#         count+=1
#     rotdig=lastdig*(10**(count-1))+remdig
#     return rotdig
# print(lasttofirst(1234))


def lefttoright(n,k):
    temp=n
    count=0
    while temp>0:
        temp//=10
        count+=1
    k%=count
    first=n//10**(count-k)
    rem=n%10**(count-k)
    rotdig=rem*(10**k)+first
    return rotdig
print(lefttoright(123456,2))




def righttoleft(n,k):
    last=n%10**k
    rem=n//10**k
    temp=n
    count=0
    while temp>0:
        temp//=10
        count+=1
    k%=count
    rotdig=last*(10**(count-k))+rem
    return rotdig
print(righttoleft(123456,2))