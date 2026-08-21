# list=[1,2,3,-5,-9,0,12]
# for num in list:
#     if num > 0:
#         print(num)
#         continue

# list=[1,2,3,-5,-9,0,12]
# for num in list:
#     if num <= 0:
#          continue
#     else:
#         print(num)


# for i in range(1,51):
#     if i % 2 != 0:
#         print(i)

# for i in range(1,51):
#     if i % 2 == 0:
#         continue
#     print(i)


# stock = {'rice':20,'wheat':25,'suger':0,'maida':2,'oil':30,'pulses':0}
# for item, quantity in stock.items():
#     if quantity == 0:
#         continue
#     print(f"{item} is available in stock with quantity {quantity}")


# stock = {'rice':20,'wheat':25,'suger':0,'maida':2,'oil':30,'pulses':0}
# items = list(stock.keys())
# i = 0
# while i < len(items):
#     item = items[i]
#     quantity = stock[item]
#     if quantity == 0:
#         i += 1
#         continue
#     print(f"{item} is available in stock with quantity {quantity}")
#     i += 1


stock = {'rice':20, 'wheat':25, 'suger':0, 'maida':2, 'oil':30, 'pulses':0}
items = list(stock.keys()) 
i = 0
while i < len(items):
    item = items[i]
    quantity = stock[item]
    i += 1
    if quantity == 0:
        continue
    print(f"{item} is available in stock with quantity {quantity}")