# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j)


# for i in range(1,11):
#     print(f"Table of {i} is")
#     for j in range(1,11):
#         print(f"{i} X {j} = {i*j}")




# l1 = ['Chicken Fried Rice','Noodles','Manchuria','chicken 65','Egg Rice','Chicken Majestic']
# l2 = ['Chicken Biryani', 'Soup', 'Chicken 65', 'Chicken Majestic','Ice cream']
# for i in l1:
#     for j in l2:
#         if i == j:
#             print(f"Common items are: {i}")


# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# total = 0
# for i in matrix:
#     for ele in i:
#         total += ele
# print(total)




# rows = int(input("Enter number of rows: "))
# columns = int(input("Enter number of columns: "))
# matrix = []
# i = 0
# while i < rows:
#     row = []
#     j = 0
#     while j < columns:
#         element = int(input("Enter element: "))
#         row.append(element)
#         j += 1
#     matrix.append(row)
#     i += 1
# print("Matrix:")
# i = 0
# while i < rows:
#     print(matrix[i])
#     i += 1
# total = 0
# i = 0
# while i < rows:
#     j = 0
#     while j < columns:
#         total += matrix[i][j]
#         j += 1
#     i += 1
# print("Total =", total)






# rows = int(input("Enter number of rows: "))
# columns = int(input("Enter number of columns: "))
# matrix = []
# i = 0
# while i < rows:
#     row = list(map(int, input().split()))
#     matrix.append(row)
#     i += 1
# print("Matrix:")
# i = 0
# while i < rows:
#     print(matrix[i])
#     i += 1
# total = 0
# i = 0
# while i < rows:
#     j = 0
#     while j < columns:
#         total += matrix[i][j]
#         j += 1
#     i += 1
# print("Total =", total)


# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j += 1
#     print()
#     i += 1


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
# for i in range(n ,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()



# n = int(input())
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print("  ", end="")
#     for j in range(i):
#         print("* ", end="")
#     print()
# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print("  ", end="")
#     for j in range(i):
#         print("* ", end="")
#     print()




# n = int(input())
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("*" * (2 * i - 1))
# for i in range(n,0,-1):
#     print(" " * (n - i), end="")
#     print("*" * (2 * i - 1))




# n=int(input())
# for i in range(1,n+1):
#     prattern=''
#     for j in range(1,i+1):
#         prattern+='*'
#     print(prattern)



# n=int(input())
# for i in range(n,0,-1):
#     prattern=''
#     for j in range(1,i+1):
#         prattern+='*'
#     print(prattern)




