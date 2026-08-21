#continue statements
# list = [17,-28,67,4,245,122,54]
# i = 0
# while i < len(list):
#     value = list[i]
#     i+=1
#     if value < 50:
#         continue
#     print(value)


# usernames = ['sumanth101', 'satyajit', '', 'uma', '', 'venky']
# while len(usernames) > 0:
#     username = usernames[0]
#     i = 0
#     while i < len(usernames) - 1:
#         usernames[i] = usernames[i + 1]
#         i+=1
#     usernames = usernames[:len(usernames) - 1]
#     if username == '':
#         continue
#     print(username)


# #or

# usernames = ['sumanth101', 'satyajit', '', 'uma', '', 'venky']
# i = 0
# while i<len(usernames):
#     username = usernames[i]
#     i+=1
#     if len(username) == 0:
#         continue
#     print(username)




sharemarcket = {'SBI':350,'HDFC':222,'ASIAN':440,'EMARELD':1010,'BOEING':110}
n = list(sharemarcket.keys())
i = 0
while i < len(sharemarcket):
    name = n[i]
    i += 1
    value = sharemarcket[name]
    if value < 400:
        continue
    print(f"{name} has {value} stocks")