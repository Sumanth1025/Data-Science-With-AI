#problem solving on string
#write a progam to swap frist and last letters or numbers
# def swap(s):
#     if len(s) < 2:
#         return s
#     else:
#         return s[-1] + s[1:-1] + s[0]
# s= input("Enter a string: ")    
# print(swap(s))



# def swap(s):
#     if len(s) < 2:
#         return s
#     result = s[-1]
#     for i in range(1, len(s) - 1):
#         result += s[i]
#     result += s[0]
#     return result
# s = input("Enter a string: ")
# print(swap(s))




# def count(s):
#     vowels = 0
#     consonants = 0
#     i = 0
#     while i < len(s):
#         ch = s[i]
#         if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or
#             ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
#             vowels += 1
#         elif ((ch >= 'a' and ch <= 'z') or
#               (ch >= 'A' and ch <= 'Z')):
#             consonants += 1
#         i += 1
#     print("Vowels:", vowels)
#     print("Consonants:", consonants)
# s = input("Enter a string: ")
# count(s)



# def count(s, ch):
#     count = 0
#     i = 0
#     while i < len(s):
#         if s[i] == ch:
#             count += 1
#         i += 1
#     return count
# s = input()
# ch = input()
# print(ch, "occurred", count(s, ch), "times")



def first(s):
    i = 0
    while i < len(s):
        count = 0
        j = 0
        while j < len(s):
            if s[i] == s[j]:
                count += 1
            j += 1
        if count == 1:
            return s[i]
        i += 1
    return "No non-repeating character"
s = input("Enter a string: ")
print("First non-repeating character:", first(s))




def last(s):
    i = len(s) - 1
    while i >= 0:
        count = 0
        j = 0
        while j < len(s):
            if s[i] == s[j]:
                count += 1
            j += 1
        if count == 1:
            return s[i]
        i -= 1
    return "No non-repeating character"
s = input("Enter a string: ")
print("Last non-repeating character:", last(s))




def remove_special(s):
    result = ""
    i = 0
    while i < len(s):
        if ((s[i] >= 'a' and s[i] <= 'z') or
            (s[i] >= 'A' and s[i] <= 'Z') or
            (s[i] >= '0' and s[i] <= '9')):
            result += s[i]
        i += 1
    return result
s = input("Enter a string: ")
print("After removing special characters:", remove_special(s))