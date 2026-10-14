import random

# #random() module is used to generate from 0.0 to 1.0
# print(random.random())


# #randint():
# #it takes two argument and generate integer between the given argument
# print(random.randint(1,5))


# #uniform()
# #it generate an random float value, here it take two arguments as range
# print(f'{random.uniform(1,10):.2f}')


# #choice():
# #It is used to choose an object from a seq of objects
# name=['uma','sai','teja']
# selectedname=random.choice(name)
# print(selectedname)


#choices():
#it used to select multiples duplicates object feom a seq
#and k is the predefine attribute for the choices



#sample():
#It is used to select multiple object from a seq without repetition



#shuffle():
#it is changing the order of object in a seq



#seed():
#




#write a ludo program to move your piece from initial point to the home point using random module there are 57 squeres in the ludo game and you have to reach from 0 to 57 using random module and the game has 4 pices and after getting 6 in first only the pice need to start and the program must need to asking me to roll dice until it reaches the home and if i want to quit means i need to insert 'q' and as it go to last it only move is the required number has come if not the move is not allowed give me the pythom code and also need to take number of players and only star if there is two players and it does not more then 4 if there are more than 4 need to add 14 more squares for each players.
import random
while True:
    try:
        players = int(input("Enter the number of players (minimum 2): "))
        if players >= 2:
            break
        print("The game needs at least 2 players.")
    except ValueError:
        print("Enter a valid number of players.")

home = 57 + max(0, players - 4) * 14
pieces = [[0, 0, 0, 0] for _ in range(players)]
current_player = 0
print("===== LUDO GAME =====")
print(f"There are {players} players and {home} squares.")
print("Each player has 4 pieces.")
print("Roll 6 to start a piece.")
print(f"Reach square {home} to win.")
print("Enter 'q' anytime to quit.")
while True:
    print(f"\nPlayer {current_player + 1}'s turn")
    print("Your pieces:")
    for i, position in enumerate(pieces[current_player]):
        if position == 0:
            print(f"Piece {i + 1}: Initial Point")
        elif position == home:
            print(f"Piece {i + 1}: HOME")
        else:
            print(f"Piece {i + 1}: Square {position}")
    choice = input("\nPress Enter to roll the dice or 'q' to quit: ")
    if choice.lower() == 'q':
        print("You quit the game!")
        break
    if choice != "":
        print("Invalid input! Press Enter or 'q'.")
        continue
    dice = random.randint(1, 6)
    print("Dice rolled:", dice)
    # Find pieces that can move
    movable = []
    for i, position in enumerate(pieces[current_player]):
        if position == 0 and dice == 6:
            movable.append(i)
        elif position > 0 and position < home:
            if position + dice <= home:
                movable.append(i)
    if len(movable) == 0:
        print("No piece can move with this dice roll.")
        current_player = (current_player + 1) % players
        continue
    # Select a piece to move
    print("\nPieces you can move:")
    for i in movable:
        print(f"Piece {i + 1} at position {pieces[current_player][i]}")
    while True:
        try:
            piece = int(input("Choose a piece number: ")) - 1
            if piece in movable:
                break
            print("Invalid choice! Select a movable piece.")
        except ValueError:
            print("Enter a valid piece number.")
    # Move the selected piece
    if pieces[current_player][piece] == 0:
        pieces[current_player][piece] = 1
        print(f"Piece {piece + 1} starts at square 1!")
    else:
        pieces[current_player][piece] += dice
        print(f"Piece {piece + 1} moved to square {pieces[current_player][piece]}.")
    # Check winning condition
    if pieces[current_player][piece] == home:
        print(f"\nPiece {piece + 1} reached HOME!")
    if all(position == home for position in pieces[current_player]):
        print(f"\nCongratulations! Player {current_player + 1} won the LUDO GAME!")
        break
    current_player = (current_player + 1) % players