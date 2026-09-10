#PositionalArga:
#write a function to welcome a student to our class
# def welcome(name,course):
#     return f'welcome {name} to 10k coders, hope you do greate in your {course} course'
# print(welcome('Balayya','Data science'))



#write a function to find area of a rectangle and circle using positional arguments
# def area(l,b,r):
#     rectangle=l*b
#     circle=3.14*r*r
#     return f'The area of rectangle is {rectangle} and the circle is {circle:.2f}'
# l=int(input())
# b=int(input())
# r=float(input())
# print(area(l,b,r))




#write a function to print count of numbers from start to stop as parameters using while loop
# def count(start, stop):
#     c = 0
#     temp=start
#     while temp <= stop:
#         c += 1
#         temp += 1
#     return f'The numbers between {start} and {stop} are: {c} '
# print(count(34,56))



#default argument
# def welcome(name='Guest'):
#     return f'welcome {name}, hope you have a greate stay at our hotal'
# print(welcome())
# print(welcome('vishal'))




#write a function to calculate total bill of a restaurant with parameters for price and deliverycharging, with rs 50 as default deliverycharging
# def total_bill(price, deliverycharging=50):
#     total = price + deliverycharging
#     return f'Total Bill: {total}'
# print(total_bill(500))




#write a function to calculate perimenter a of circle with parameters for radius and pi and pass default value for pi
# def pericir(r,pi=3.14):
#     perimeter=2*pi*r
#     return f'perimenter of the circle of radius {r} is: {perimeter:.2f}'
# print(pericir(23))