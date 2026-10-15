import time
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
