# #NEsted while loop
# i = 1
# while i < 6:
#     j = 1
#     while j < 6:
#         print(i,j)
#         j += 1
#     i += 1

# write a nested while loop to calculate total and average of 5 students
# students=1
# while students<=5:
#     total=0
#     marks=1
#     while marks<=5:
#         score=int(input(f"Enter marks of student {students} subject {marks}: "))
#         total+=score
#         marks+=1
#     average=total/5
#     print(f"Total marks of student {students}: {total}")
#     print(f"Average marks of student {students}: {average}")
#     students+=1


#a resturant has 3 customers and each one placed 4 items ordered calculate total bill of each customer with 12%gst
# customers=1
# while customers<=3:
#     totalbill=0
#     items=1
#     while items<=4:
#         price=float(input(f"Enter price of item {items} for customer {customers}: "))
#         totalbill+=price
#         items+=1
#     gst=totalbill*0.12
#     final_bill=totalbill+gst
#     print(f"Total bill for customer {customers} before GST: {totalbill}")
#     print(f"GST amount for customer {customers}: {gst}")
#     print(f"Final bill for customer {customers} after GST: {final_bill}")
#     customers+=1


#track monthly expense of a person for 3 months for 4 cateories in each month and print the highest expense in all three months
# month=1
# highest=0
# while month <= 3:
#     total=0
#     category=1
#     while category <= 4:
#         expense=float(input(f"Enter expense for month {month} category {category}: "))
#         total+=expense
#         category+=1
#     print(f"Total expense for month {month}: {total}")
#     if total > highest:
#         highest=total
#     month+=1
# print(f"Highest expense: {highest}")




# runs = []
# players = []
# for player_number in range(1, 12):
# 	player_name = input(f"Enter name of player {player_number}: ")
# 	total_runs = 0
# 	innings = 1
# 	while innings <= 2:
# 		score = int(input(f"Enter runs scored by {player_name} in innings {innings}: "))
# 		total_runs += score
# 		innings += 1
# 	players.append(player_name)
# 	runs.append(total_runs)
# print("\nTest Match Scoreboard")
# for player_number in range(11):
# 	print(f"{players[player_number]}: {runs[player_number]} runs")
# highest_score = runs[0]
# man_of_the_match = players[0]
# for player_number in range(1, 11):
# 	if runs[player_number] > highest_score:
# 		highest_score = runs[player_number]
# 		man_of_the_match = players[player_number]
# print(f"\nMan of the Match: {man_of_the_match} ({highest_score} runs)")







# # create a daskboard to runs scored by each players in a test cricket match and give man of the match to the 
# # person with highest score. that means create an list and give man of the match to the heighest score person
# runs = []
# players = []
# for i in range(1, 12):
#     total_runs = 0
#     innings = 1
#     while True:
#         score = int(input(f"Enter runs scored by player {i} in innings {innings}: "))
#         total_runs += score
#         if innings == 2:
#             break
#         innings += 1
#     players.append(i)
#     runs.append(total_runs)
# print("\nTest Match Scoreboard")
# for i in range(11):
#     print(f"Player {players[i]}: {runs[i]} runs")
# highest_score = runs[0]
# man_of_the_match = players[0]
# for i in range(1, 11):
#     if runs[i] > highest_score:
#         highest_score = runs[i]
#         man_of_the_match = players[i]
# print(f"\nMan of the Match: Player {man_of_the_match} - {highest_score} runs")






runs = []
players = []
for i in range(1, 12):
    total_runs = 0
    ball = 1
    print(f"\nPlayer {i}")
    while True:
        score = int(input(f"Enter runs for ball {ball}: "))
        if score == -1:
            print(f"Player {i} is OUT!")
            break
        total_runs += score
        ball += 1
    players.append(i)
    runs.append(total_runs)
print("\n==============================")
print("      TEST MATCH SCOREBOARD     ")
print("================================")
for i in range(11):
    print(f"Player {players[i]} : {runs[i]} runs")
print("=================================")
highest_score = runs[0]
man_of_the_match = players[0]
for i in range(1, 11):
    if runs[i] > highest_score:
        highest_score = runs[i]
        man_of_the_match = players[i]
print(f"\nMan of the Match")
print(f"Player {man_of_the_match} - {highest_score} runs")