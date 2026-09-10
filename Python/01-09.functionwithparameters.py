# def table(n):
#     for i in range(1,11):
#         print(f'{n}X{i}=={n*i}')
# n=int(input())
# table(n)


#write a function to calculate area and perameter of a function
# def arenpri(l,b):
#     area=l*b
#     peri=2*(l+b)
#     print(f'Area of the rectangle with length {l} and with the bredth {b} is: {area}')
#     print(f'perimeter of the rectangle with length {l} and with the bredth {b} is: {peri}')
# l=int(input())
# b=int(input())    
# arenpri(l,b)




#write a function to find greater among 3 numbers
# def greater(a,b,c):
#     if a>b and a>c:
#         print(f'{a} is greater among the three numbers')
#     elif b>c:
#         print(f'{b} is greater among the three numbers')
#     else:
#         print(f'{c} is greater among the three numbers')
# a=int(input())
# b=int(input())
# c=int(input())
# greater(a,b,c)




#write a function smallest among three number
# def smallest(a,b,c):
#     if a<b and a<c:
#         print(f'{a} is smallest among the three numbers')
#     elif b<c:
#         print(f'{b} is smallest among the three numbers')
#     else:
#         print(f'{c} is smallest among the three numbers')
# a=int(input())
# b=int(input())
# c=int(input())
# smallest(a,b,c)


# write a func to calculate discount price by passing mrp and discount as argument
# def mrpdis(MRP, discount):
#     discount_amount = MRP * discount / 100
#     price = MRP - discount_amount
#     return price
# MRP = float(input("Enter MRP: "))
# discount = float(input("Enter discount percentage: "))
# print("Discount price:", mrpdis(MRP, discount))




#calculate age of the person
# def agecal(birthyear,currentyear):
#     age=currentyear-birthyear
#     return age
# print(agecal(2005,2026))




#write a function to calculate total marks and another function for percentage of that total
# def total_marks(m1, m2, m3, m4, m5):
#     return m1 + m2 + m3 + m4 + m5
# def percentage(total):
#     return total / 5
# total = total_marks(60, 80, 68.79, 90, 75)
# print("Total Marks:", total)
# print("Percentage:", f"{percentage(total):.1f}", "%")






#write a function to calculate total expenses of a company and second function calculate the sales os the company and the thired function takes the above function as argument and calculate the revenue of the company
# Function to calculate total expenses
def total_expenses(s, r, e, t):
    return s + r + e + t
def total_sales(p1, p2, p3):
    return p1 + p2 + p3
def revenue(expenses, sales):
    result = sales - expenses
    if result > 0:
        print("Profit:", result)
    elif result < 0:
        print("Loss:", abs(result))
    else:
        print("No Profit No Loss")
expenses = total_expenses(50000, 20000, 10000, 5000)
sales = total_sales(30000, 20000, 10000)
print("Total Expenses:", expenses)
print("Total Sales:", sales)
revenue(expenses, sales)