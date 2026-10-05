# list1=[1,2,3,4,5]
# lambfunc=lambda num:num*num
# mapFunc=map(lambfunc,list1)
# print(list(mapFunc))

# write a lambda function to convert a string to upper case and map to a tuple of names using 
#maps function
names=['Bharat','tiger','Dabanng','kick','ready']
lambfunc=lambda name:name.upper()
caseCon=map(lambfunc,names)
print(list(caseCon))
