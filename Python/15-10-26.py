import time
#"editor.inlineSuggest.enabled": false,
#Time module(): It is used for timestamps 
#sleep():
#it is used to pass the execution of the program a certain second
# def timer(num):
#     while num>=0:
#         print(num)
#         time.sleep(1)
#         num-=1
#     print('Time up!')
# timer(10)

#time():
#It return the number of seconds passed since jan 1st 1970 till now
# print(time.time())

# def prime(a,b):
#     starttime=time.time()
#     print(f'{time.ctime(starttime)}')
#     for num in range(a,b+1):
#         count=0
#         for i in range(1,num+1):
#             if num%i==0:
#                 count+=1
#         if count==2:
#             print(f'{num} is prime')
#     stoptime=time.time() 
#     print(f'{time.ctime(stoptime)}')
#     timetakem=stoptime-starttime
#     print(f'The time takento execute this program is:{round(timetakem,4)}')   
# prime(1,100)

#ctime():
#It is used to convert a timestamp into readable format
# print(time.ctime())


#localtime():
#   It also convert a timestanp into readable format but breakes them each attribute into seperate parts
# currenttime=time.localtime()
# print(currenttime)
# print(currenttime.tm_year)
# print(currenttime.tm_yday)


#use localtime and print each induial parts if i give month it need to print month like wise
def cuti(a):
    cuti=time.localtime()
    if a=='year':
        print(cuti.tm_year)
    elif a=='month':
        print(cuti.tm_mon)
    elif a=='day':
        print(cuti.tm_mday)
    elif a=='hour':
        print(cuti.tm_hour)
    elif a=='minute':
        print(cuti.tm_min)
    elif a=='second':
        print(cuti.tm_sec)
    elif a=='weekday':
        print(cuti.tm_wday)
    elif a=='yearday':
        print(cuti.tm_yday)
    else:
        print('Invalid input')
cuti('month')



#surftime():

present=time.strftime('%d-%m-%y')
print(present)