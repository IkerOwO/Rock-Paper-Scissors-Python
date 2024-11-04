import random

def game(player, bot): 
    print(f'Player Chooses {player}')
    print(f'Bot Chooses {bot}')

    if player == bot:
        print("Draw")
    elif (player == "Rock" and bot == "Scissors") or \
        (player == "Paper" and bot == "Rock") or \
        (player == "Scissors" and bot == "Paper"):
        print("You Win :3")
    else:
        print("You Lose :(")

print("Welcome to Rock | Paper | Scissors")
player = str(input("Player's Turn (Rock, Paper o Scissors): "))
things = ['Rock', 'Paper', 'Scissors']
bot = random.choice(things)

if player in things:
    game(player, bot)
else:
    print("Not a valid Option, please choose Rock, Paper or Scissors.")
        