#Dictinories
a={'keys':'values'}
print (type(a))
print(a)


#{'Keys':'values'}--->{'str' : 'str'}
a.items()
print(a.items()) 


#values, pop, etc
c = {'name':'krishna', 'age':21, 'address':'hydebrad'}
print(c)


#bank eg:
f={'name':'uma', 'bankid':'ICICI25674','amount':5000}
print(f)

#adding or removing values
f['amount']+=500
print(f)

f['amount']-=1000
print(f)

#To print speficic value
print(f['name'])


#sets
d = {1,2,3,4,5342,463,242,1,2,4}
print(d)
e = {5,6,3,8,9,2}
print(e)
#Union
print(d|e)
#Intersection
print(d&e)
#Difference
print(d-e)
print(e-d)
#Symmetric Difference
print(d^e)