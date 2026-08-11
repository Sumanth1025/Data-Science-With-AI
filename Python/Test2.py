
# #1
# visitors = [120, 150, 140, 180, 200, 170, 160]
# found = 0
# position = 0
# for i in range(1, 6):
#     if visitors[i] > visitors[i - 1] and visitors[i] > visitors[i + 1]:
#         if found == 0:
#             position = i
#             found = 1
# if found == 1:
#     print("First peak:", visitors[position])



# #2
# balance = 1000
# transactions = [500, -300, -1200, 800]
# for transaction in transactions:
#     balance = balance + transaction
#     if balance < 0:
#         print("Overdrawn")
#     elif balance == 0:
#         print("Empty")
#     else:
#         print(balance)


# #3
# temperatures = [20, 22, 25, 21, 23, 26, 28, 24]
# current = 1
# longest = 1
# for i in range(1, 8):
#     if temperatures[i] > temperatures[i - 1]:
#         current = current + 1
#     else:
#         current = 1
#     if current > longest:
#         longest = current
# print("Longest increasing streak:", longest)


# #4
# number = 75824
# score = 0
# position = 0
# for digit in str(number):
#     position = position + 1
#     digit = int(digit)
#     if digit > 5:
#         score = score + position
#     elif digit == 5:
#         score = score + 5
#     else:
#         score = score - 1
# print("Score:", score)


# #5
# temperatures = [20, 25, 25, 30, 28, 35]
# score = 0
# for i in range(1, 6):
#     if temperatures[i] > temperatures[i - 1]:
#         score = score + 2
#     elif temperatures[i] < temperatures[i - 1]:
#         score = score - 1
#     else:
#         score = score + 0
# print("Score:", score)
# if score > 5:
#     print("Rapidly Increasing")
# elif score < 0:
#     print("Mostly Decreasing")
# else:
#     print("Stable")


# #6
# transactions = [500, -200, 300, -100, 700, -50]
# alternating = 1
# for i in range(1, 6):
#     if transactions[i] > 0 and transactions[i - 1] > 0:
#         alternating = 0
#     elif transactions[i] < 0 and transactions[i - 1] < 0:
#         alternating = 0
# if alternating == 1:
#     print("Pattern is alternating")
# else:
#     print("Pattern is broken")


# #7
# score = 0
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         score +=15
#     elif i % 3 == 0:
#         score +=3
#     elif i % 5 == 0:
#         score +=5
#     else:
#         score += 1
# print("Score:", score)


# #8
# numbers = [10, 17, 5, 20, 14]
# largest = 0
# for i in range(1, 5):
#     gap = numbers[i] - numbers[i - 1]
#     if gap < 0:
#         gap = gap * -1
#     if gap > largest:
#         largest = gap
# print("Largest gap:", largest)


# #9
# commands = [5, 8, -4, -15, 6]
# position = 0
# for command in commands:
#     position = position + command
#     if position > 10:
#         print("Right Zone")
#     elif position < -10:
#         print("Left Zone")
#     else:
#         print("Safe Zone")


# #10
# prices = [100, 105, 103, 110, 115, 112, 120]
# trendScore = 0
# for i in range(1, 7):
#     if prices[i] > prices[i - 1]:
#         trendScore = trendScore + 1
#     elif prices[i] < prices[i - 1]:
#         trendScore = trendScore - 1
#     else:
#         trendScore = trendScore + 0
# print("Trend Score:", trendScore)
# if trendScore > 2:
#     print("Bullish")
# elif trendScore < -2:
#     print("Bearish")
# else:
#     print("Neutral")