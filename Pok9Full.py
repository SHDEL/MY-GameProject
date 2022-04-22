#Pokdeng 52 ใบ
print("----Pokdeng----")
import time
import random

#startgame
print("please enter \"start\" to play")

start = "start"
start_cmnd = -1

while start_cmnd != start :
    start_cmnd = str(input(" "))
    if start_cmnd == start:
        print("please wait...")
    else :
        print("please enter \"start\" to play")
        continue

#make a card list
ca_A = ['A♠','A♥','A♦','A♣']
ca_2 = ['2♠','2♥','2♦','2♣']
ca_3 = ['3♠','3♥','3♦','3♣']
ca_4 = ['4♠','4♥','4♦','4♣']
ca_5 = ['5♠','5♥','5♦','5♣']
ca_6 = ['6♠','6♥','6♦','6♣']
ca_7 = ['7♠','7♥','7♦','7♣']
ca_8 = ['8♠','8♥','8♦','8♣']
ca_9 = ['9♠','9♥','9♦','9♣']
ca_10 =['10♠','10♥','10♦','10♣']
ca_j = ['J♠','J♥','J♦','J♣']
ca_q = ['Q♠','Q♥','Q♦','Q♣']
ca_k = ['K♠','K♥','K♦','K♣']

playerca_1 = -5
playerca_2 = -10
playerpt1 = 0
playerpt2 = 0
botpt1 = 0
botpt2 = 0
time.sleep(1.5)
while True:

	if playerca_1 != playerca_2:
		ca_spade = ['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠']
		ca_heart = ['A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥']
		ca_diamonds = ['A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦']
		ca_clubs = ['A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣']

		deck = ca_spade + ca_heart + ca_diamonds + ca_clubs 
		random.shuffle(deck)

		time.sleep(1.5)
		print('----------------------------')
		#playerdraw
		print("Player Draw Turn")
		time.sleep(1.5)
		playerca_1 = random.choice(deck)
		deck.remove(playerca_1)
		playerca_2 = random.choice(deck)
		print("Your Cards: ", playerca_1, "," ,playerca_2)

		#botdraw
		print('bot drawing cards....')
		time.sleep(1)
		deck.remove(playerca_2)
		botca_1 = random.choice(deck)
		deck.remove(botca_1)
		botca_2 = random.choice(deck)

		#playercard point
		#playerca_1
		if playerca_1 in ca_A : 
			playerpt1 += 1
			print('Your point is: ',playerpt1)

		elif playerca_1 in ca_2 :
			playerpt1 += 2
			print('Your point is: ',playerpt1)
		
		elif playerca_1 in ca_3 :
			playerpt1 += 3
			print('Your point is: ',playerpt1)
		
		elif playerca_1 in ca_4 :
			playerpt1 += 4
			print('Your point is: ',playerpt1)
		
		elif playerca_1 in ca_5 :
			playerpt1 += 5
			print('Your point is: ',playerpt1)
		
		elif playerca_1 in ca_6 :
			playerpt1 += 6
			print('Your point is: ',playerpt1)
		
		elif playerca_1 in ca_7 :
			playerpt1 += 7
			print('Your point is: ',playerpt1)
		
		elif playerca_1 in ca_8 :
			playerpt1 += 8
			print('Your point is: ',playerpt1)
		
		elif playerca_1 in ca_9 :
			playerpt1 += 9
			print('Your point is: ',playerpt1)
		
		elif playerca_1 in ca_10 :
			playerpt1 += 0
			print('Your point is: ',playerpt1)
		
		elif playerca_1 in ca_j :
			playerpt1 += 0
			print('Your point is: ',playerpt1)
		
		elif playerca_1 in ca_q :
			playerpt1 += 0
			print('Your point is: ',playerpt1)
		
		elif playerca_1 in ca_k :
			playerpt1 += 0
			print('Your point is: ',playerpt1)
		
		#playerca_2

		if playerca_2 in ca_A :
			playerpt2 += 1
			print('Your point2 is: ',playerpt2)
		
		elif playerca_2 in ca_2 :
			playerpt2 += 2
			print('Your point is: ',playerpt2)
	
		elif playerca_2 in ca_3 :
			playerpt2 += 3
			print('Your point is: ',playerpt2)
		
		elif playerca_2 in ca_4 :
			playerpt2 += 4
			print('Your point is: ',playerpt2)
		
		elif playerca_2 in ca_5 :
			playerpt2 += 5
			print('Your point is: ',playerpt2)
		
		elif playerca_2 in ca_6 :
			playerpt2 += 6
			print('Your point is: ',playerpt2)
		
		elif playerca_2 in ca_7 :
			playerpt2 += 7
			print('Your point is: ',playerpt2)
		
		elif playerca_2 in ca_8 :
			playerpt2 += 8
			print('Your point is: ',playerpt2)
		
		elif playerca_2 in ca_9 :
			playerpt2 += 9
			print('Your point is: ',playerpt2)
		
		elif playerca_2 in ca_10 :
			playerpt2 += 0
			print('Your point is: ',playerpt2)
		
		elif playerca_2 in ca_j :
			playerpt2 += 0
			print('Your point is: ',playerpt2)
		
		elif playerca_2 in ca_q :
			playerpt2 += 0
			print('Your point is: ',playerpt2)
		
		elif playerca_2 in ca_k :
			playerpt2 += 0
			print('Your point is: ',playerpt2)
		
		time.sleep(1.5)
		playerpt = playerpt1 + playerpt2
		while playerpt >= 10 and playerpt <= 20:
			playerpt -= 10
			break
		print('Your total point is: ',playerpt)
		print('----------------------------')
		
		#botpoint
		#botca_1
		if botca_1 in ca_A :
			botpt1 += 1

		elif botca_1 in ca_2 :
			botpt1 += 2
		
		elif botca_1 in ca_3 :
			botpt1 += 3
		
		elif botca_1 in ca_4 :
			botpt1 += 4
		
		elif botca_1 in ca_5 :
			botpt1 += 5
		
		elif botca_1 in ca_6 :
			botpt1 += 6
		
		elif botca_1 in ca_7 :
			botpt1 += 7
		
		elif botca_1 in ca_8 :
			botpt1 += 8
		
		elif botca_1 in ca_9 :
			botpt1 += 9
		
		elif botca_1 in ca_10 :
			botpt1 += 0
		
		elif botca_1 in ca_j :
			botpt1 += 0
		
		elif botca_1 in ca_q :
			botpt1 += 0
		
		elif botca_1 in ca_k :
			botpt1 += 0
		
		#botca_2

		if botca_2 in ca_A :
			botpt2 += 1
		
		elif botca_2 in ca_2 :
			botpt2 += 2
	
		elif botca_2 in ca_3 :
			botpt2 += 3
		
		elif botca_2 in ca_4 :
			botpt2 += 4
		
		elif botca_2 in ca_5 :
			botpt2 += 5
		
		elif botca_2 in ca_6 :
			botpt2 += 6
		
		elif botca_2 in ca_7 :
			botpt2 += 7
		
		elif botca_2 in ca_8 :
			botpt2 += 8
		
		elif botca_2 in ca_9 :
			botpt2 += 9
		
		elif botca_2 in ca_10 :
			botpt2 += 0
		
		elif botca_2 in ca_j :
			botpt2 += 0
		
		elif botca_2 in ca_q :
			botpt2
		
		elif botca_2 in ca_k :
			botpt2 += 0
		
		time.sleep(1.5)
		botpt = botpt1 + botpt2
		while botpt >= 10 and botpt <= 20 :
			botpt -= 10
			break

	#gamerule
	#playerpoint with botpoint
	if playerpt != botpt:
		#pok
		if playerpt1 == 9 and playerpt2 == 9:
			print('You Win!')
			print('Pok9')
			print('Bot point is: ',botpt)

		elif playerpt1 == 8 and playerpt2 == 8:
			print('You Win!')
			print('Pok8')
			print('Bot point is: ',botpt)

		elif botpt1 == 9 and botpt2 == 9:
			print('You Lose!')
			print('Bot got Pok9')
			print('Bot point is: ',botpt)

		elif botpt1 == 8 and botpt2 == 8:
			print('You Lose!')
			print('Bot got Pok8')
			print('Bot point is: ',botpt)

		elif playerpt > botpt:
			print('You Win!')
			print('Bot point is: ',botpt)

		elif playerpt < botpt:
			print('You Lose!')
			print('Bot point is: ',botpt)
		
		elif playerpt == botpt:
			print('Draw!')
			print('Bot point is: ',botpt)
		
		print('Bot Cards is: ',botca_1, "," ,botca_2)
		print('If you want to play again please enter "restart" or enter "exit" to quit the game')
		restart = 'restart'
		restart_cmd = str(input(' '))
		if restart_cmd == restart :
			print('please wait...')
			time.sleep(1.0)
		if restart_cmd == 'exit' :
			print('please wait...')
			print('Quit game...')
			time.sleep(1.0)
			exit()
		while restart_cmd != restart and 'exit' :
			print('please enter "restart" or "exit"')
			restart_cmd = str(input(' '))
			if restart_cmd == restart :
				print('please wait...')
				time.sleep(1.0)
			if restart_cmd == 'exit' :
				print('please wait...')
				print('Quit game...')
				time.sleep(1.0)
				exit()
			continue
	continue


	