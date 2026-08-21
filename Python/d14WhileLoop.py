# s=0
# while s<=10:
#     if s%2==0:
#         print(s)
#     s+=1

# s=0
# while s<=25:
#     if s%2==0:
#         print(s)
#     s+=1



# s=0
# while s<=25:
#     if s%2!=0:
#         print(s)
#     s+=1


# s=0
# i=1
# while i<=100:
#     s+=i
#     i+=1
# print(s)



# str1 ='python'
# i=0
# while i<len(str1):
#     print(str1[i])
#     i+=1

# s = int(input("Enter a number: "))
# i= 1
# while i<=10:
#     print(f"{s} X {i} = {s*i}")
# #or print(s,"X",i,"=",s*i)
#     i+=1 


# i=1
# while i<=30:
#     if i%3==0:
#         print(i)
#     i+=1


# str1 = input("Enter a string: ")
# i = len(str1) - 1
# while i >= 0:
#     print(str1[i], end="")
#     i -= 1


# secretNum = 44
# guess = int(input("Guess the secret number (between 1 and 100): "))
# while guess != secretNum:
#     if guess < secretNum:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")
#     guess = int(input("Enter your guess: "))
# print("Congratulations! You guessed the secret number.")



# import random
# secretNum = random.randint(1, 100)
# guess = int(input("Guess the secret number (between 1 and 100): "))
# while guess != secretNum:
#     if guess < secretNum:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")
#     guess = int(input("Enter your guess: "))
# print("Congratulations! You guessed the secret number.")



prices = [1299,1399,1599,2599,3699,7999]
new_prices = []
i = 0
while i < len(prices):
    gst = prices[i] * 0.12
    new_price = prices[i] + gst
    new_prices.append(new_price)
print(new_prices)