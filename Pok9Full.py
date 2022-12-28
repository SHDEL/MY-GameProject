import random
import time
from utilities import Utilities

# Pokdeng 52 ใบ
print("----Pokdeng----")

# startgame
print("please enter \"start\" to play")

start = "start"
start_cmnd = -1

while start_cmnd != start:
    start_cmnd = str(input(" "))
    if start_cmnd == start:
        print("please wait...")
    else:
        print("please enter \"start\" to play")

# make a card list
ca_A = ['A♠', 'A♥', 'A♦', 'A♣']
ca_2 = ['2♠', '2♥', '2♦', '2♣']
ca_3 = ['3♠', '3♥', '3♦', '3♣']
ca_4 = ['4♠', '4♥', '4♦', '4♣']
ca_5 = ['5♠', '5♥', '5♦', '5♣']
ca_6 = ['6♠', '6♥', '6♦', '6♣']
ca_7 = ['7♠', '7♥', '7♦', '7♣']
ca_8 = ['8♠', '8♥', '8♦', '8♣']
ca_9 = ['9♠', '9♥', '9♦', '9♣']
ca_10 = ['10♠', '10♥', '10♦', '10♣']
ca_j = ['J♠', 'J♥', 'J♦', 'J♣']
ca_q = ['Q♠', 'Q♥', 'Q♦', 'Q♣']
ca_k = ['K♠', 'K♥', 'K♦', 'K♣']

# Since all these variables will surely and eventually reassign before using,
# there's no need to initialize it but declare its type instead.
playerca_1: str
playerca_2: str
playerpt1: int
playerpt2: int
botpt1: int
botpt2: int
time.sleep(1.5)
while True:

    ca_spade = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠',
                '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']
    ca_heart = ['A♥', '2♥', '3♥', '4♥', '5♥', '6♥',
                '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥']
    ca_diamonds = ['A♦', '2♦', '3♦', '4♦', '5♦', '6♦',
                   '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦']
    ca_clubs = ['A♣', '2♣', '3♣', '4♣', '5♣', '6♣',
                '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']

    deck = ca_spade + ca_heart + ca_diamonds + ca_clubs
    random.shuffle(deck)

    time.sleep(1.5)
    print('----------------------------')
    # playerdraw
    print("Player Draw Turn")
    time.sleep(1.5)
    playerca_1 = random.choice(deck)
    deck.remove(playerca_1)
    playerca_2 = random.choice(deck)
    print("Your Cards: ", playerca_1, ",", playerca_2)

    # botdraw
    print('bot drawing cards....')
    time.sleep(1)
    deck.remove(playerca_2)
    botca_1 = random.choice(deck)
    deck.remove(botca_1)
    botca_2 = random.choice(deck)

    # playercard point
    # playerca_1
    playerpt1 = Utilities.getPoint(playerca_1)
    print(f"Your point is: {playerpt1}")
    playerpt2 = Utilities.getPoint(playerca_2)
    print(f"Your point is: {playerpt2}")

    time.sleep(1.5)

    # No need to use loop
    # while playerpt >= 10 and playerpt <= 20:
    # 	playerpt -= 10
    # 	break

    # only single if should be enough
    playerpt = Utilities.getTotalPointInPokdeng(playerpt1 + playerpt2)

    print('Your total point is: ', playerpt)
    print('----------------------------')

    # botpoint
    # botca_1
    botpt1 = Utilities.getPoint(botca_1)

    # botca_2
    botpt2 = Utilities.getPoint(botca_2)

    time.sleep(1.5)
    botpt = Utilities.getTotalPointInPokdeng(botpt1 + botpt2)

    # gamerule
    # playerpoint with botpoint

    # pok
    if playerpt == 9:
        print('You Win!')
        print('Pok9')
        print('Bot point is: ', botpt)

    elif playerpt == 8:
        print('You Win!')
        print('Pok8')
        print('Bot point is: ', botpt)

    elif botpt == 9:
        print('You Lose!')
        print('Bot got Pok9')
        print('Bot point is: ', botpt)

    elif botpt == 8:
        print('You Lose!')
        print('Bot got Pok8')
        print('Bot point is: ', botpt)

    elif playerpt > botpt:
        print('You Win!')
        print('Bot point is: ', botpt)

    elif playerpt < botpt:
        print('You Lose!')
        print('Bot point is: ', botpt)

    elif playerpt == botpt:
        print('Draw!')
        print('Bot point is: ', botpt)

    print('Bot Cards is: ', botca_1, ",", botca_2)
    print('If you want to play again please enter "restart" or enter "exit" to quit the game')

    restartStr = 'restart'
    exitStr = 'exit'
    restart_cmd: str = None

    while restart_cmd != restartStr and restart_cmd != exitStr:
        restart_cmd = str(input(' '))
        if restart_cmd == restartStr:
            print('please wait...')
            time.sleep(1.0)
            break
        if restart_cmd == exitStr:
            print('please wait...')
            print('Quit game...')
            time.sleep(1.0)
            exit()
        print('please enter "restart" or "exit"')
