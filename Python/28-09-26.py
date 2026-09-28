# list1=[1,2,3,4,5,6,7,8,9,10]
# tuple1=tuple(num for num in list1 if num%5==0)
# print(tuple1)




#write a comprehension to generate a tuple from a list of numbers 1 to 50 such that replace all even numbers with 0 
# and odd numbers with 1. 
# binaryTuple=tuple(0 if num%2==0 else 1 for num in range(1,51))
# print(binaryTuple)



#write a comprehension to genetate a tuple of only non empty names
# names=['venkat','sumanth','umamaheshwar','','rasagna','','durga','','saratha']
# tuple1=tuple(name for name in names if name)
# print(tuple1)



#write a comprehension to genetate a tuple from a range of numbers 1 to 50 such that the number divided by 3 but not 5 
# nums=tuple(num for num in range(1,51) if num%3==0 and num%5!=0)
# print(nums)



#write a comprehension to generate a tuple for selling price by adding discount such that if the price greater 
# than 25000 give 11% discount else give 7% discount
# prices=[12999,23999,45999,37999,11999,57999,88999]
# sellpri=tuple(i-(i*0.11) if i>25000 else i-(i*0.07) for i in prices)
# print(sellpri)