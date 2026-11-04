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


# def lefttoright(n,k):
#     temp=n
#     count=0
#     while temp>0:
#         temp//=10
#         count+=1
#     k%=count
#     first=n//10**(count-k)
#     rem=n%10**(count-k)
#     rotdig=rem*(10**k)+first
#     return rotdig
# print(lefttoright(123456,2))




# def righttoleft(n,k):
#     last=n%10**k
#     rem=n//10**k
#     temp=n
#     count=0
#     while temp>0:
#         temp//=10
#         count+=1
#     k%=count
#     rotdig=last*(10**(count-k))+rem
#     return rotdig
# print(righttoleft(123456,2))



                                            #String(30-10-26)
# #WAP to convert a camel case string to snake case string
# def cameltosnake(string):
#     snakecase=''
#     i=0
#     while i<len(string):
#         if 'A'<=string[i]<='Z':
#             snakecase+='_'
#             snakecase+=chr(ord(string[i])+32)
#         else:
#             snakecase+=string[i]
#         i+=1
#     return snakecase
# print(cameltosnake('sumanthTeja'))


# # WAP to convert a string from snake case to camel case
# def snaketocamel(String):
#     camelcase=''
#     i=0
#     while i<len(String):
#         if String[i]!='_':
#             camelcase+=String[i]
#             i+=1
#         else:
#             camelcase+=chr(ord(String[i+1])-32)
#             i+=2
#     return camelcase
# print(snaketocamel('sumanth_teja'))




# def revthesen(string):
#     reverse=''
#     word=''
#     i=0
#     while i<len(string):
#         if string[i]==' ':
#             reverse=word+' '+reverse
#             word=''
#         else:
#             word+=string[i]
#         i+=1
#     reverse=word+' '+reverse
#     print(reverse)
# revthesen("python is easy")




# def revthesen(string):
#     reverse=''
#     word=''
#     i=0
#     while i<len(string):
#         if string[i] == ' ':
#             j=len(word)-1
#             while j>=0:
#                 reverse+=word[j]
#                 j-=1
#             reverse+=' '
#             word=''
#         else:
#             word+=string[i]
#         i+=1
#     j=len(word)-1
#     while j>=0:
#         reverse+=word[j]
#         j-=1
#     print(reverse)
# revthesen("python is easy")





# def reverse_odd(s):
#     result=""
#     odd=""
#     i=0
#     while i<len(s):
#         if i%2!= 0:
#             odd=s[i]+odd
#         else:
#             result+=s[i]
#         i+=1
#     final=""
#     i=0
#     j=0
#     while i<len(s):
#         if i%2==0:
#             final+=s[i]
#         else:
#             final+=odd[j]
#             j+=1
#         i+=1
#     return final
# s = input("Enter a string: ")
# print(reverse_odd(s))




# def reverse_odd(s):
#     result=""
#     odd=""
#     i=0
#     while i<len(s):
#         if i%2!=0:
#             odd=s[i]+odd
#         else:
#             result+=s[i]
#         i+=1
#     final=""
#     j=0
#     i=0
#     for ch in s:
#         if i%2==0:
#             final+=ch
#         else:
#             final+=odd[j]
#             j+=1
#         i+=1
#     return final
# s=input("Enter a string: ")
# print(reverse_odd(s))




def reverse_odd(s):
    odd=""
    i=0
    while i<len(s):
        if i%2!=0:
            odd=s[i]+odd
        i+=1
    return "".join(s[i] if i%2==0 else odd[i//2] for i in range(len(s)))
s=input("Enter a string:")
print(reverse_odd(s))




# def compress(s):
#     result=""
#     i=0
#     while i<len(s):
#         count=1
#         while i+1<len(s) and s[i]==s[i + 1]:
#             count+=1
#             i+=1
#         result+=s[i]+str(count)
#         i+=1
#     return result
# s="aaabbccccdde"
# print(compress(s))




# def decompress(s):
#     result = ""
#     i = 0
#     while i<len(s):
#         ch=s[i]
#         i+=1
#         count=0
#         while i<len(s) and '0'<=s[i]<='9':
#             count = count*10+int(s[i])
#             i+=1
#         result+=ch*count
#     return result
# s="a3b2c4d2e1"
# print(decompress(s))