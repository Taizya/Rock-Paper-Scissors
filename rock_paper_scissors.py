# definition of player object to track number of wins for each player

class Player:
    def __init__(self):
        self.wins = 0

    def add_win(self):
        self.wins += 1


# creating an instance of each player in the game
player1 = Player()
player2 = Player()

# infinite while loop
while True:
    print("Do you want to start a new game? ")
    new_game = input("Enter 1 if yes , enter 0 if no: ")
    if int(new_game) == 0:
        break
    elif int(new_game) == 1:
        print("Best of three")
        print("Rock = 0, Paper = 1, Scissors = 2")

        rounds = 1
        while rounds < 4:

            print("Start Game")
            print("Player1 pick a number for your move")
            player_1 = int(input("Player1:  "))

            print("Next Player2 pick a number for your move")
            player_2 = int(input("Player2: "))

            if player_1 > 2 or player_2 > 2:
                print("your input is invalid")
                break

            elif player_1 < 0 or player_2 < 0:
                print("your input is invalid")
                break

            if (player_1 == 0 and player_2 == 2) or (player_1 == 2 and player_2 == 0):
                if player_1 == 0:
                    print(f"Player 1 wins round {rounds}")
                    player1.add_win()
                else:
                    print(f"Player 2 wins round {rounds}")
                    player2.add_win()
            elif (player_1 == 2 and player_2 == 1) or (player_1 == 1 and player_2 == 2):
                if player_1 == 2:
                    print(f"Player 1 wins round {rounds}")
                    player1.add_win()
                else:
                    print(f"Player 2 wins round {rounds}")
                    player2.add_win()
            elif (player_1 == 1 and player_2 == 0) or (player_1 == 1 and player_2 == 0):
                if player_1 == 1:
                    print(f"Player 2 wins round {rounds}")
                    player2.add_win()
                else:
                    print(f"Player 1 wins round {rounds}")
                    player1.add_win()

            if rounds >= 2:
                if player1.wins > player2.wins:
                    print("player 1 wins the game")
                    break
                else:
                    print("player 2 wins the game")
                    break
            rounds += 1
    else:
        print("Your input is invalid, Please chose 1 or 0")
