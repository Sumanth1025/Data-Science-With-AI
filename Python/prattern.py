# k=5
# for i in range(1,k+1):
#     for j in range(1,k+1):
#         print('*',end=' ')
#     print()




# k=4
# l=8
# for i in range(1,k+1):
#     for j in range(1,l+1):
#         print('*',end=' ')
#     print()






# k=5
# for i in range(1,k+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()





# k=5
# for i in range(k,0,-1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()




# k=5
# for i in range(1,k+1):
#     for l in range(k-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()




# k=5
# for i in range(k,0,-1):
#     for l in range(k-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()



k = 5
for i in range(1,k+1):
    print(' '*(k-i),end='')
    print('*'*(2*i-1))