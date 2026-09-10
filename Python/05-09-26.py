# def valid_data(d,m,y):
    
# def isprime(n):
#     count=0
#     for i in range(1,n+1):
#         if n % i == 0:
#             count+=1
#     if count==2:
#         print(f'The number {n} is a prime number')
#     else:
#         print(f'The number {n} is not a prime number')
# isprime(7)



# def primenum(n, m):
#     count_prime = 0
#     for num in range(m, n + 1):
#         if num < 2:
#             continue
#         count = 0
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 count += 1
#         if count == 2:
#             print(num)
#             count_prime += 1
#     print("Total prime numbers:", count_prime)
# primenum(20, 5)


# def primenum(m,n):
#     count_prime = 0
#     first_prime = None
#     last_prime = None
#     for num in range(m, n + 1):
#         if num < 2:
#             continue
#         count = 0
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 count += 1
#         if count == 2:
#             count_prime += 1
#             if first_prime is None:
#                 first_prime = num
#             last_prime = num
#     print("Total prime numbers:", count_prime)
#     print("First prime:", first_prime)
#     print("Last prime:", last_prime)
# primenum(5,20)



def closestprime(m,n):
    distance = 0
    while True:
        back = n - distance
        front = n + distance
        if back >= 2:
            count = 0
            for i in range(1, back + 1):
                if back % i == 0:
                    count += 1
            if count == 2:
                print("Closest prime:", back)
                break
        if front != back:
            count = 0
            for i in range(1, front + 1):
                if front % i == 0:
                    count += 1
            if count == 2:
                print("Closest prime:", front)
                break
        distance += 1
closestprime(5,20)




# def sunny(n):
#     num = n + 1
#     for i in range(1, num + 1):
#         if i * i == num:
#             return "Sunny number"
#     return "Not a sunny number"
# print(sunny(15))


# def sunnyNum(num):
#     temp = num+1
#     if temp**0.5 == int(temp**0.5):
#         print(f"{num} is sunny number")
#     else:
#         print(f'{num} is not sunny number')
# sunnyNum(15)



# def primenum(n,m):
#     total = 0
#     for num in range(m, n + 1):
#         count = 0
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 count += 1
#         if count == 2:
#             print(num)
#             total += num
#     print("Sum of prime numbers:", total)
#     count = 0
#     for i in range(1, total + 1):
#         if total % i == 0:
#             count += 1
#     if count == 2:
#         print("Venkat number")
#     else:
#         print("Not a Venkat number")
# primenum(20,5)
# primenum(7,2)



# def neon(n):
#     s=n*n
#     a=0
#     while s>0:
#         b=s%10
#         a+=b
#         s//=10
#     if a==n:
#         print(f'{n} is a neon number')
#     else:
#         print(f'{n} is not a neon number')
# neon(9)


# def armstrong(num):
#     temp = num
#     total = 0
#     digits = len(str(num))
#     while temp > 0:
#         digit = temp % 10
#         total += digit ** digits
#         temp //= 10
#     if total == num:
#         print(f"{num} is an Armstrong number")
#     else:
#         print(f"{num} is not an Armstrong number")
# armstrong(153)