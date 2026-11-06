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
#     # return f'{rotdig}'
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




# def reverse_odd(s):
#     odd=""
#     i=0
#     while i<len(s):
#         if i%2!=0:
#             odd=s[i]+odd
#         i+=1
#     return "".join(s[i] if i%2==0 else odd[i//2] for i in range(len(s)))
# s=input("Enter a string:")
# print(reverse_odd(s))




# def compress(s):
#     result=""
#     i=0
#     while i<len(s):
#         count=1
#         while i+1<len(s) and s[i]==s[i + 1]:
#             count+=1
#             i+=1
#         result+=s[i]+f'{count}'
#         i+=1
#     return result
# s="aaabbccccdde"
# print(compress(s))




# def decompress(s):
#     result=""
#     i=0
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






# def compress(s):
#     result=""
#     count=1
#     i=1
#     while i<len(s):
#         if s[i]==s[i-1]:
#             count+=1
#         else:
#             result+=s[i-1]+f'{count}'
#             count=1
#         i+=1
#     result+=s[i-1]+f'{count}'
#     return result
# s="aaabbccccdde"
# print(compress(s))





# def decompress(s):
#     result=""
#     i=0
#     while i<len(s):
#         ch=s[i]
#         i+=1
#         digit=0
#         num=0
#         while i<len(s) and '0'<=s[i]<='9':
#             digit=ord(s[i])-ord('0')    
#             num=num*10+digit
#             i+=1
#         result+=ch*num
#     return result
# s="a10b2c4d2e1"
# print(decompress(s))





#check wheather words are anagram

# def anagrams(a,b):
#     if len(a)!=len(b):
#         return 'Anagram not possible'
#     i=0
#     count1=0
#     count2=0
#     while i<len(a):
#         j=0
#         while j<len(a):
#             if a[i]==a[j]:
#                 count1+=1
#             if a[i]==b[j]:
#                 count2+=1
#             j+=1
#         if count1!=count2:
#             return 'Not an anagram'
#         i+=1
#     return 'Strings are anagram'
# print(anagrams('silent','listen'))

# print(anagrams())




# def conveersion(sentence):
#     i=0
#     words=[]
#     word=''
#     while i<len(sentence):
#         if sentence[i]!=' ':
#             word+=sentence[i]
#         else:
#             words+=[word]
#             word=''
#         i+=1
#     words+=[word]
#     return words
# sen='My name is sumanth'
# print(conveersion(sen))



# #WAP to print all anagram to a target value fron a sentence

# def anagrams(a,b):
#     if len(a)!=len(b):
#         return False
#     i=0
#     while i<len(a):
#         j = 0
#         count1=0
#         count2=0
#         while j<len(a):
#             if a[i]==a[j]:
#                 count1+=1
#             if a[i]==b[j]:
#                 count2+=1
#             j+=1
#         if count1!=count2:
#             return False
#         i+=1
#     return True
# def conversion(sentence, target):
#     i=0
#     word=''
#     result = []
#     while i<len(sentence):
#         if sentence[i]!=' ':
#             word+=sentence[i]
#         else:
#             if anagrams(word,target):
#                 result+=[word]
#             word=''
#         i+=1
#     if word!='':
#         if anagrams(word,target):
#             result+=[word]
#     return result
# sentence = "silent listen enlist hello inlets cat"
# target = "listen"
# print(conversion(sentence, target))


#----------------------------------------------------------------------------
# def anagrams(a, b):
#     if len(a) != len(b):
#         return False
#     count=[0]*26
#     i = 0
#     while i < len(a):
#         count[ord(a[i]) - 97] += 1
#         count[ord(b[i]) - 97] -= 1
#         i += 1
#     return count==[0]*26
# def find_anagrams(sentence,target):
#     result=[]
#     word=''
#     i=0
#     sentence+=' '
#     while i<len(sentence):
#         if sentence[i]!=' ':
#             word+=sentence[i]
#         else:
#             if word and anagrams(word,target):
#                 result+=[word]
#             word=''
#         i+=1
#     return result
# sentence = "silent listen enlist hello inlets cat"
# target = "listen"
# print(find_anagrams(sentence, target))




# def higest(list):
#     i=0
#     h=list[0]+list[1]
#     while i<len(list):
#         j=i+1
#         while j<len(list):
#             b=list[i]+list[j]
#             if b>h:
#                 h=b
#             j+=1
#         i+=1
#     return h
# list=[1,5,8,10,7,-1,-5]
# print(higest(list))




# def numtorom(num):
#     syms=['M','CM','D','CD','c','XC','L','XL','X','IX','V','IV','I']
#     vals=[1000,900,500,400,100, 90,  50,  40, 10,  9,   5,  4, 1]
#     roman=''
#     i=0
#     while num>0:
#         count=num//vals[i]
#         roman+=syms[i]*count
#         num%=vals[i]
#         i+=1
#     return roman
# print(numtorom(2578))
# print(numtorom(1995))

                                                                        #"editor.inlineSuggest.enabled": false,


# def romtonum(Rom):
#     syms=['M','CM','D','CD','c','XC','L','XL','X','IX','V','IV','I']
#     vals=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
#     result=0
#     i=0
#     while i<len(Rom):
#         j=0
#         while j<len(syms):
#             if i+1<len(Rom) and Rom[i]+Rom[i+1]==syms[j]:
#                 result+=vals[j]
#                 i+=2
#                 break
#             elif Rom[i]==syms[j]:
#                 result+=vals[j]
#                 i+=1
#                 break
#             j+=1
#     return result
# print(romtonum('MCMXCV'))


# sort the digits of a number in ascending order
def numsort(num):
    freq=[0]*10
    sortednum=0
    temp=num
    while temp>0:
        digit=temp%10
        freq[digit]+=1
        temp//=10
    i=0
    while i<len(freq):
        if freq[i]>0:
            sortednum=sortednum*10+i
            freq[i]-=1
            i-=1
        i+=1
    return sortednum
print(numsort(1995))
