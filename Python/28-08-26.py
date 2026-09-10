# n=int(input())
# count=0
# i=1
# while i<=n:
#     if n%i==0:
#         count+=1
#     i+=1
# print(f'The number of factors{n} are: {count}')



#even and odd list
# m = int(input('Enter starting number: '))
# n = int(input('Enter the ending number: '))
# temp = m
# evencount = 0
# oddcount = 0
# evenlist = []
# oddlist = []
# while temp <= n:
#     if temp % 2 == 0:
#         evenlist += [temp]
#         evencount += 1
#     else:
#         oddlist += [temp]
#         oddcount += 1
#     temp += 1
# print(f'The list of even numbers from {m} to {n} is: {evenlist}')
# print(f'The list of odd numbers from {m} to {n} is: {oddlist}')
# print(f'The number of even numbers from {m} to {n} are: {evencount} and the odd numbers are: {oddcount}')



#reversing string
# s=input('Enter the string:')
# print(s[::-1])

# s=input('Enter the string:')
# rev = ''
# i=0
# while i < len(s):
#     rev = s[i]+rev
#     i+=1
# print(rev)


# s=input('Enter the string:')
# rev = ''
# i=0
# while i < len(s):
#     rev = s[i]+rev
#     i+=1
# print(f'The reverse of the string {s} is {rev}')
# if s==rev:
#     print('The given string {s} is palindrome')
# else:
#     print('The given string {s} is not palindrome')














# #counting the vowles in a string
# s = input('Enter the string:')
# count = 0
# i = 0
# while i < len(s):
#     if s[i] in 'aeiou':
#         count += 1
#     i += 1
# print("Number of vowels:", count)



# #print vowles
# s = input('Enter the string:')
# vowels = ''
# i = 0
# while i < len(s):
#     if s[i] in 'aeiou':
#         vowels += s[i]
#     i += 1
# print("Vowels:", vowels)



# # unique vowles only
# s = input('Enter the string:')
# vowels = ''
# i = 0
# while i < len(s):
#     if s[i] in 'aeiou' and s[i] not in vowels:
#         vowels += s[i]
#     i += 1
# print("Vowels:", vowels)



# #count consonants
# s = input('Enter the string:')
# count = 0
# i = 0
# while i < len(s):
#     if s[i] not in 'aeiou':
#         count += 1
#     i += 1
# print("Number of consonants:", count)



# #count for alp, num and splchr
# s=input('Enter the string: ')
# aplcount=0
# numcount=0
# splcount=0
# i=0
# while i<len(s):
#     if s[i].isalpha():
#         aplcount += 1
#     elif s[i].isdigit():
#         numcount += 1
#     else:
#         splcount += 1
#     i += 1
# print("Alphabets:", aplcount)
# print("Numbers:", numcount)
# print("Special characters:", splcount)


# #or

# s = input('Enter the string: ')
# aplcount = 0
# numcount = 0
# splcount = 0
# i = 0
# while i < len(s):
#     if ('a' <= s[i] <= 'z') or ('A' <= s[i] <= 'Z'):
#         aplcount += 1
#     elif '0' <= s[i] <= '9':
#         numcount += 1
#     else:
#         splcount += 1
#     i += 1
# print("Alphabets:", aplcount)
# print("Numbers:", numcount)
# print("Special characters:", splcount)