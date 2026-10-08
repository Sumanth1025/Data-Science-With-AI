# marks=[('Ram',89),('Rahul',32),('Shreya',90),('Smriti',56),('Gangadhar',99)]
# print(sorted(marks,key=lambda x: x[1]))


# empRec={'Vasudha':45000,'Rasagna':99000,'Venkat':12000,'Shankar':110000,'Sumanth':25000}
# print(sorted(empRec.items(),key=lambda x:x[1]))


from functools import reduce
# nums=[1,2,3,4,5]
# print(reduce(lambda num1,num2: num1+num2,nums))


#finding the largest number using reduce
# nums=(45,76,34,12,89,90,56,345,876,11,22,10)
# print(reduce(lambda n1,n2: n1 if n1>n2 else n2,nums))


#first is price and second is quantity. now based on the calculate total using reduce
cart = [(456,3),(112,5),(767,2),(234,3)]
print(reduce(lambda x,y:x+(y[0]*y[1]),cart,0))
