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




# sharemarcket = {'SBI':350,'HDFC':222,'ASIAN':440,'EMARELD':1010,'BOEING':110}
# n = list(sharemarcket)
# i = 0
# while i < len(sharemarcket):
#     name = n[i]
#     i += 1
#     value = sharemarcket[name]
#     if value < 400:
#         continue
#     print(f"{name} has {value} stocks")



# marks={'Durga':98,'Rasagnya':76,'venkat':32,'sumanth':78,'Uma':30,'Banu teja':89}
# n = list(marks)
# i = 0
# while i < len(marks):
#     p = n[i]
#     i+=1
#     if marks[p] <= 35:
#         continue
#     print(f"{p} has passed the test")



#pass: It hold the place in the code where we come and edit the logic or condition any thing in the code in the future
#eg
# class sumanth:
#     pass
# def future():
#     pass
# i=0
# if i < 10:
#     pass
