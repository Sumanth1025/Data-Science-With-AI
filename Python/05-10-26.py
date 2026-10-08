# list1=[1,2,3,4,5]
# lambfunc=lambda num:num*num
# mapFunc=map(lambfunc,list1)
# print(list(mapFunc))

# write a lambda function to convert a string to upper case and map to a tuple of names using 
#maps function
# names=['Bharat','tiger','Dabanng','kick','ready']
# lambfunc=lambda name:name.upper()
# caseCon=map(lambfunc,names)
# print(list(caseCon))


# write a lambda function to add 12% gst if price less than 50000 else
#add 18% gst if price geater then 50000 and map it to a list 
#of prices using map function
# prices=[72000,64000,69000,34000,23000,55000,18000]
# lambfun=lambda price:price+(price*0.12) if price<50000 else price+(price*0.18)
# gst=list(map(lambfun,prices))
# print(gst)


# write a lambda function to check whether a num is greater than 550 and
#  less than 800 and pass it to filter function to filter out the numbers
# which satisfies the function in a seq


# nums=[345,766,233,987,445,770,293,900]
# lambfun=lambda num:num>550 and num<800
# filtered=filter(lambfun,nums)
# print(list(filtered))

#write a lambda function to filter out salaries which are greater then 50000
#from a lis of salaries using filter function

# salaries=[75000,45000,56000,34000,23000,55000,18000]
# lamfun= lambda salary:salary>50000
# filtered=tuple(filter(lamfun,salaries))
# print(filtered)

# celebs=['prabhasraju@]bheemavarma.com','janvikapoor@bolly.com','peddi@appalavalasacom','jadalparadise.com']
# lamf=lambda email:'@' in email and '.' in email
# valid_emails=list(filter(lamf,celebs))
# print(valid_emails)