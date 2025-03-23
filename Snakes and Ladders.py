import random

snake_ladder_board = []
for row in range(9, -1, -1):
    rows = []
    for col in range(1, 11):
        rows.append(f"{col + row * 10:<4}")
        
    if row % 2:
        snake_ladder_board.append(''.join(rows[::-1]))
    else:
        snake_ladder_board.append(''.join(rows))

print('\n'.join(snake_ladder_board))

players_move = {}

snakes = {}
ladders = {}
snake = 0
lst = list(range(11, 100))

while snake < 11:
    x = random.choice(lst)
    lst.remove(x)
    target = random.choice(list(set(range(1, (x//10) * 10)) - set(snakes.values())))
    snakes[x] = target
    snake += 1

print("Snakes:", snakes)

snake_squares = set(snakes.keys()).union(set(snakes.values()))
lst = list(set(range(2, 90)) - snake_squares)
ladder = 0

while ladder < 11:
    x = random.choice(lst)
    lst.remove(x)
    target = random.choice(list(set(range(((x + 10)//10) * 10, 99)) - snake_squares))
    ladders[x] = target
    ladder += 1

print("Ladders:", ladders)

number_of_players = int(input("Enter the number of players: "))

for i in range(1, number_of_players + 1):
    players_move[i] = 0
    
winner_decided = False
turn = 1

while not winner_decided:
    player = 1
    while player <= number_of_players:
        number = random.randint(1, 6)
        print(f"Turn {turn}: Player {player} rolled {number}")
        
        if players_move[player] + number <= 100:
            players_move[player] += number

        # Check for snakes or ladders AFTER moving
        if players_move[player] in ladders:
            print(f"Player {player} climbs ladder to {ladders[players_move[player]]}")
            players_move[player] = ladders[players_move[player]]
        elif players_move[player] in snakes:
            print(f"Player {player} bitten by snake, falls to {snakes[players_move[player]]}")
            players_move[player] = snakes[players_move[player]]
        
        # Check if the player won
        if players_move[player] == 100:
            print(f"Player {player} wins the game! 🎉")
            winner_decided = True
            break
        
        # Allow another turn if rolling a 6
        if number != 6:
            player += 1
        
    turn += 1
