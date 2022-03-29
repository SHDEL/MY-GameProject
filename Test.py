#Pokdeng 52 ใบ
print("----Pokdeng----")
import time
import random
ca_spade = ['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠']
ca_heart = ['A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥']
ca_diamonds = ['A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦']
ca_clubs = ['A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣']

deck = ca_spade + ca_heart + ca_diamonds + ca_clubs 
random.shuffle(deck)

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

# ca_A = ['A♠','A♥','A♦','A♣']
# ca_2 = ['2♠','2♥','2♦','2♣']
# ca_3 = ['3♠','3♥','3♦','3♣']
# ca_4 = ['4♠','4♥','4♦','4♣']
# ca_5 = ['5♠','5♥','5♦','5♣']
# ca_6 = ['6♠','6♥','6♦','6♣']
# ca_7 = ['7♠','7♥','7♦','7♣']
# ca_8 = ['8♠','8♥','8♦','8♣']
# ca_9 = ['9♠','9♥','9♦','9♣']
# ca_10 =['10♠','10♥','10♦','10♣']
# ca_j = ['J♠','J♥','J♦','J♣']
# ca_q = ['Q♠','Q♥','Q♦','Q♣']
# ca_k = ['K♠','K♥','K♦','K♣']

playerpt1 = 0
playerpt2 = 0
botpt1 = 0
botpt2 = 0
print('----------------------------')
time.sleep(1.5)

if playerca_1 != playerca_2:
    #playercard point
    # ca_A = ['A♠','A♥','A♦','A♣']
    if playerca_1 or playerca_2 == 'A♠' :
        if playerca_1 == 'A♠':
            playerpt1 +=1
            print('Your point is: ', playerpt1)
                
        elif playerca_2 == 'A♠':
            playerpt2 +=1
            print('Your point is: ', playerpt2)
                
    if playerca_1 or playerca_2 == 'A♥' :
        if playerca_1 == 'A♥':
                playerpt1 += 1
                print('Your point is: ', playerpt1)
                
        elif playerca_2 == 'A♥': 
                playerpt2 +=1
                print('Your point is: ', playerpt2)
                
    if playerca_1 or playerca_2 == 'A♦' :
        if playerca_1 == 'A♦':
                playerpt1 +=1
                print('Your point is: ', playerpt1)
                
        elif playerca_2 == 'A♦':
                playerpt2 +=1
                print('Your point is: ', playerpt2)
                
    if playerca_1 or playerca_2 == 'A♣':
        if playerca_1 == 'A♣':
                playerpt1 += 1
                print('Your point is: ',playerpt1)
                
        elif playerca_2 == 'A♣':
                playerpt2 += 1
                print('Your point is: ',playerpt2)
        # ca_2 = ['2♠','2♥','2♦','2♣']
    if playerca_1 or playerca_2 == '2♠':
        if playerca_1 == '2♠':
                playerpt1 += 2
                print('Your point is: ',playerpt1)

        elif playerca_2 == '2♠':
                playerpt2 += 2
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '2♥':
        if playerca_1 == '2♥':
                playerpt1 +=2
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '2♥':
                playerpt2 += 2
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '2♦':
        if playerca_1 == '2♦':
                playerpt1 += 2
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '2♦':
                playerpt2 += 2
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '2♣':
        if playerca_1 == '2♣':
                playerpt1 += 2
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '2♣':
                playerpt2 += 2
                print('Your point is: ',playerpt2)
        # ca_3 = ['3♠','3♥','3♦','3♣']
    if playerca_1 or playerca_2 == '3♠':
        if playerca_1 == '3♠':
                playerpt1 += 3
                print('Your point is: ',playerpt1)

        elif playerca_2 == '3♠':
                playerpt2 += 3
                print('Your point is: ',playerpt2)
            
    if playerca_1 or playerca_2 == '3♥':
        if playerca_1 == '3♥':
                playerpt1 += 3
                print('Your point is: ',playerpt1)

        elif playerca_2 == '3♥':
                playerpt2 += 3
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '3♦':
        if playerca_1 == '3♦':
                playerpt1 += 3
                print('Your point is: ',playerpt1)

        elif playerca_2 == '3♦':
                playerpt2 += 3
                print('Your point is: ',playerpt2)
            
    if playerca_1 or playerca_2 == '3♣':
        if playerca_1 == '3♣':
                playerpt1 += 3
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '3♣':
                playerpt2 += 3
                print('Your point is: ',playerpt2)
        # ca_4 = ['4♠','4♥','4♦','4♣']
    if playerca_1 or playerca_2 == '4♠':
        if playerca_1 == '4♠':
                playerpt1 += 4
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '4♠':
                playerpt2 += 4
                print('Your point is: ',playerpt2)
            
    if playerca_1 or playerca_2 == '4♥':
        if playerca_1 == '4♥':
                playerpt1 += 4
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '4♥':
                playerpt2 += 4
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '4♦':
        if playerca_1 == '4♦':
                playerpt1 += 4
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '4♦':
                playerpt2 += 4
                print('Your point is: ',playerpt2)
            
    if playerca_1 or playerca_2 == '4♣':
        if playerca_1 == '4♣':
                playerpt1 += 4
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '4♣':
                playerpt2 += 4
                print('Your point is: ',playerpt2)
        # ca_5 = ['5♠','5♥','5♦','5♣']
    if playerca_1 or playerca_2 == '5♠':
        if playerca_1 == '5♠':
                playerpt1 +=5
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '5♠':
                playerpt2 += 5
                print('Your point is: ',playerpt2)
            
    if playerca_1 or playerca_2 == '5♥':
        if playerca_1 == '5♥':
                playerpt1 +=5
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '5♥':
                playerpt2 += 5
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '5♦':
        if playerca_1 == '5♦':
                playerpt1 += 5
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '5♦':
                playerpt2 += 5
                print('Your point is: ',playerpt2)

    if playerca_1 or playerca_2 == '5♣':
        if playerca_1 == '5♣':
                playerpt1 +=5
                print('Your point is: ',playerpt1)

        elif playerca_2 == '5♣':
                playerpt2 += 5
                print('Your point is: ',playerpt2)
        # ca_6 = ['6♠','6♥','6♦','6♣']
    if playerca_1 or playerca_2 == '6♠':
        if playerca_1 == '6♠':
                playerpt1 += 6
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '6♠':
                playerpt2 += 6
                print('Your point is: ',playerpt2)

    if playerca_1 or playerca_2 == '6♥':
        if playerca_1 == '6♥':
                playerpt1 += 6
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '6♥':
                playerpt2 += 6
                print('Your point is: ',playerpt2)
    
    if playerca_1 or playerca_2 == '6♦':
        if playerca_1 == '6♦':
                playerpt1 += 6
                print('Your point is: ',playerpt1)
        
        elif playerca_2 == '6♦':
                playerpt2 += 6
                print('Your point is: ',playerpt2)

    if playerca_1 or playerca_2 == '6♣':
        if playerca_1 == '6♣':
                playerpt1 += 6
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '6♣':
                playerpt2 += 6
                print('Your point is: ',playerpt2)
        # ca_7 = ['7♠','7♥','7♦',]
    if playerca_1 or playerca_2 == '7♠':
        if playerca_1 == '7♠':
                playerpt1 += 7
                print('Your point is: ',playerpt1)
        
        elif playerca_2 == '7♠':
                playerpt2 += 7
                print('Your point is: ',playerpt2)
            
    if playerca_1 or playerca_2 == '7♥':
        if playerca_1 == '7♥':
                playerpt1 += 7
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '7♥':
                playerpt2 += 7
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '7♦':
        if playerca_1 == '7♦':
                playerpt1 += 7
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '7♦':
                playerpt2 += 7
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '7♣':
        if playerca_1 == '7♣':
                playerpt1 += 7
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '7♣':
                playerpt2 += 7
                print('Your point is: ',playerpt2)
        # ca_8 = ['8♠','8♥','8♦','8♣']
    if playerca_1 or playerca_2 == '8♠':
        if playerca_1 == '8♠':
                playerpt1 += 8
                print('Your point is: ',playerpt1)

        elif playerca_2 == '8♠':
                playerpt2 += 8
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '8♥':
        if playerca_1 == '8♥':
                playerpt1 += 8
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '8♥':
                playerpt2 += 8
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '8♦':
        if playerca_1 == '8♦':
                playerpt1 += 8
                print('Your point is: ',playerpt1)

        elif playerca_2 == '8♦':
                playerpt2 += 8
                print('Your point is: ',playerpt2)

    if playerca_1 or playerca_2 == '8♣':
        if playerca_1 == '8♣':
                playerpt1 += 8
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '8♣':
                playerpt2 += 8
                print('Your point is: ',playerpt2)
        # ca_9 = ['9♠','9♥','9♦','9♣']
    if playerca_1 or playerca_2 == '9♠':
        if playerca_1 == '9♠':
                playerpt1 += 9
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '9♠':
                playerpt2 += 9
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '9♥':
        if playerca_1 == '9♥':
                playerpt1 += 9
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '9♥':
                playerpt2 += 9
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '9♦':
        if playerca_1 == '9♦':
                playerpt1 += 9
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '9♦':
                playerpt2 += 9
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '9♣':
        if playerca_1 == '9♣':
                playerpt1 += 9
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '9♣':
                playerpt2 += 9
                print('Your point is: ',playerpt2)
        # ca_10 =['10♠','10♥','10♦','10♣']
    if playerca_1 or playerca_2 == '10♠':
        if playerca_1 == '10♠':
                playerpt1 += 0
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '10♠':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '10♥':
        if playerca_1 == '10♥':
                playerpt1 += 0
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '10♥':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '10♦':
        if playerca_1 == '10♦':
                playerpt1 += 0
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '10♦':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == '10♣':
        if playerca_1 == '10♣':
                playerpt1 += 0
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == '10♣':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
        # ca_j = ['J♠','J♥','J♦','J♣']
    if playerca_1 or playerca_2 == 'J♠':
        if playerca_1 == 'J♠':
                playerpt1 += 0
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == 'J♠':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == 'J♥':
        if playerca_1 == 'J♥':
                playerpt1 += 0
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == 'J♥':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == 'J♦':
        if playerca_1 == 'J♦':
                playerpt1 += 0
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == 'J♦':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == 'J♣':
        if playerca_1 == 'J♣':
                playerpt1 += 0
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == 'J♣':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
        # ca_q = ['Q♠','Q♥','Q♦','Q♣']
    if playerca_1 or playerca_2 == 'Q♠':
        if playerca_1 == 'Q♠':
                playerpt1 += 0
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == 'Q♠':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == 'Q♥':
        if playerca_1 == 'Q♥':
                playerpt1 += 0
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == 'Q♥':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == 'Q♦':
        if playerca_1 == 'Q♦':
                playerpt1 += 0
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == 'Q♦':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == 'Q♣':
        if playerca_1 == 'Q♣':
                playerpt1 += 0
                print('Your point is: ',playerpt1)

        elif playerca_2 == 'Q♣':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
        # ca_k = ['K♠','K♥','K♦','K♣']
    if playerca_1 or playerca_2 == 'K♠':
        if playerca_1 == 'K♠':
                playerpt1 += 0
                print('Your point is: ',playerpt1)

        elif playerca_2 == 'K♠':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == 'K♥':
        if playerca_1 == 'K♥':
                playerpt1 += 0
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == 'K♥':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
        
    if playerca_1 or playerca_2 == 'K♦':
        if playerca_1 == 'K♦':
                playerpt1 += 0
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == 'K♦':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
    if playerca_1 or playerca_2 == 'K♣':
        if playerca_1 == 'K♣':
                playerpt1 += 0
                print('Your point is: ',playerpt1)
            
        elif playerca_2 == 'K♣':
                playerpt2 += 0
                print('Your point is: ',playerpt2)
    time.sleep(1.5)
    playerpt = (playerpt1 + playerpt2)
while playerpt >= 10 and playerpt <= 20:
    playerpt -= 10
    break
print('Your total point is: ',playerpt)


#botpoint
if botca_1 != botca_2:
    # ca_A = ['A♠','A♥','A♦','A♣']
    if botca_1 or botca_2 == 'A♠' :
        if botca_1 == 'A♠':
            botpt1 +=1
                
        elif botca_2 == 'A♠':
            botpt2 +=1
                
    if botca_1 or botca_2 == 'A♥' :
        if botca_1 == 'A♥':
                botpt1 += 1
                
        elif botca_2 == 'A♥': 
                botpt2 +=1
                
    if botca_1 or botca_2 == 'A♦' :
        if botca_1 == 'A♦':
                botpt1 +=1
                
        elif botca_2 == 'A♦':
                botpt2 +=1
                
    if botca_1 or botca_2 == 'A♣':
        if botca_1 == 'A♣':
                botpt1 += 1
                
        elif botca_2 == 'A♣':
                botpt2 += 1
        # ca_2 = ['2♠','2♥','2♦','2♣']
    if botca_1 or botca_2 == '2♠':
        if botca_1 == '2♠':
                botpt1 += 2

        elif botca_2 == '2♠':
                botpt2 += 2
        
    if botca_1 or botca_2 == '2♥':
        if botca_1 == '2♥':
                botpt1 +=2
            
        elif botca_2 == '2♥':
                botpt2 += 2
        
    if botca_1 or botca_2 == '2♦':
        if botca_1 == '2♦':
                botpt1 += 2
            
        elif botca_2 == '2♦':
                botpt2 += 2
        
    if botca_1 or botca_2 == '2♣':
        if botca_1 == '2♣':
                botpt1 += 2
            
        elif botca_2 == '2♣':
                botpt2 += 2
        # ca_3 = ['3♠','3♥','3♦','3♣']
    if botca_1 or botca_2 == '3♠':
        if botca_1 == '3♠':
                botpt1 += 3

        elif botca_2 == '3♠':
                botpt2 += 3
            
    if botca_1 or botca_2 == '3♥':
        if botca_1 == '3♥':
                botpt1 += 3

        elif botca_2 == '3♥':
                botpt2 += 3
        
    if botca_1 or botca_2 == '3♦':
        if botca_1 == '3♦':
                botpt1 += 3

        elif botca_2 == '3♦':
                botpt2 += 3
            
    if botca_1 or botca_2 == '3♣':
        if botca_1 == '3♣':
                playerpt1 += 3
            
        elif botca_2 == '3♣':
                botpt2 += 3
        # ca_4 = ['4♠','4♥','4♦','4♣']
    if botca_1 or botca_2 == '4♠':
        if botca_1 == '4♠':
                botpt1 += 4
            
        elif botca_2 == '4♠':
                botpt2 += 4
            
    if botca_1 or botca_2 == '4♥':
        if botca_1 == '4♥':
                botpt1 += 4
            
        elif botca_2 == '4♥':
                botpt2 += 4
        
    if botca_1 or botca_2 == '4♦':
        if botca_1 == '4♦':
                botpt1 += 4
            
        elif botca_2 == '4♦':
                botpt2 += 4
            
    if botca_1 or botca_2 == '4♣':
        if botca_1 == '4♣':
                botpt1 += 4
            
        elif botca_2 == '4♣':
                botpt2 += 4
        # ca_5 = ['5♠','5♥','5♦','5♣']
    if botca_1 or botca_2 == '5♠':
        if botca_1 == '5♠':
                botpt1 +=5
            
        elif botca_2 == '5♠':
                botpt2 += 5
            
    if botca_1 or botca_2 == '5♥':
        if botca_1 == '5♥':
                botpt1 +=5
            
        elif botca_2 == '5♥':
                botpt2 += 5
        
    if botca_1 or botca_2 == '5♦':
        if botca_1 == '5♦':
                botpt1 += 5
            
        elif botca_2 == '5♦':
                botpt2 += 5

    if botca_1 or botca_2 == '5♣':
        if botca_1 == '5♣':
                botpt1 +=5

        elif botca_2 == '5♣':
                botpt2 += 5
        # ca_6 = ['6♠','6♥','6♦','6♣']
    if botca_1 or botca_2 == '6♠':
        if botca_1 == '6♠':
                botpt1 += 6
            
        elif botca_2 == '6♠':
                botpt2 += 6

    if botca_1 or botca_2 == '6♥':
        if botca_1 == '6♥':
                botpt1 += 6
            
        elif botca_2 == '6♥':
                botpt2 += 6
    
    if botca_1 or botca_2 == '6♦':
        if botca_1 == '6♦':
                botpt1 += 6
        
        elif botca_2 == '6♦':
                botpt2 += 6
        
    if botca_1 or botca_2 == '6♣':
        if botca_1 == '6♣':
                botpt1 += 6
            
        elif botca_2 == '6♣':
                botpt2 += 6
        # ca_7 = ['7♠','7♥','7♦',]
    if botca_1 or botca_2 == '7♠':
        if botca_1 == '7♠':
                botpt1 += 7
        
        elif botca_2 == '7♠':
                botpt2 += 7
            
    if botca_1 or botca_2 == '7♥':
        if botca_1 == '7♥':
                botpt1 += 7
            
        elif botca_2 == '7♥':
                botpt2 += 7
        
    if botca_1 or botca_2 == '7♦':
        if botca_1 == '7♦':
                botpt1 += 7
            
        elif botca_2 == '7♦':
                botpt2 += 7
        
    if botca_1 or botca_2 == '7♣':
        if botca_1 == '7♣':
                botpt1 += 7
            
        elif botca_2 == '7♣':
                botpt2 += 7
        # ca_8 = ['8♠','8♥','8♦','8♣']
    if botca_1 or botca_2 == '8♠':
        if botca_1 == '8♠':
                botpt1 += 8

        elif botca_2 == '8♠':
                botpt2 += 8
        
    if botca_1 or botca_2 == '8♥':
        if botca_1 == '8♥':
                botpt1 += 8
            
        elif botca_2 == '8♥':
                botpt2 += 8
        
    if botca_1 or botca_2 == '8♦':
        if botca_1 == '8♦':
                botpt1 += 8

        elif botca_2 == '8♦':
                botpt2 += 8

    if botca_1 or botca_2 == '8♣':
        if botca_1 == '8♣':
                botpt1 += 8
            
        elif botca_2 == '8♣':
                botpt2 += 8
        # ca_9 = ['9♠','9♥','9♦','9♣']
    if botca_1 or botca_2 == '9♠':
        if botca_1 == '9♠':
                botpt1 += 9
            
        elif botca_2 == '9♠':
                botpt2 += 9
        
    if botca_1 or botca_2 == '9♥':
        if botca_1 == '9♥':
                botpt1 += 9
            
        elif botca_2 == '9♥':
                botpt2 += 9
        
    if botca_1 or botca_2 == '9♦':
        if botca_1 == '9♦':
                botpt1 += 9
            
        elif botca_2 == '9♦':
                botpt2 += 9
        
    if botca_1 or botca_2 == '9♣':
        if botca_1 == '9♣':
                botpt1 += 9
            
        elif botca_2 == '9♣':
                botpt2 += 9
        # ca_10 =['10♠','10♥','10♦','10♣']
    if botca_1 or botca_2 == '10♠':
        if botca_1 == '10♠':
                botpt1 += 0
            
        elif botca_2 == '10♠':
                botpt2 += 0
        
    if botca_1 or botca_2 == '10♥':
        if botca_1 == '10♥':
                botpt1 += 0
            
        elif botca_2 == '10♥':
                botpt2 += 0
        
    if botca_1 or botca_2 == '10♦':
        if botca_1 == '10♦':
                botpt1 += 0
            
        elif botca_2 == '10♦':
                botpt2 += 0
        
    if botca_1 or botca_2 == '10♣':
        if botca_1 == '10♣':
                botpt1 += 0
            
        elif botca_2 == '10♣':
                botpt2 += 0
        # ca_j = ['J♠','J♥','J♦','J♣']
    if botca_1 or botca_2 == 'J♠':
        if botca_1 == 'J♠':
                botpt1 += 0
            
        elif botca_2 == 'J♠':
                botpt2 += 0
        
    if botca_1 or botca_2 == 'J♥':
        if botca_1 == 'J♥':
                botpt1 += 0
            
        elif botca_2 == 'J♥':
                botpt2 += 0
        
    if botca_1 or botca_2 == 'J♦':
        if botca_1 == 'J♦':
                botpt1 += 0
            
        elif botca_2 == 'J♦':
                botpt2 += 0
        
    if botca_1 or botca_2 == 'J♣':
        if botca_1 == 'J♣':
                botpt1 += 0
            
        elif botca_2 == 'J♣':
                botpt2 += 0

        # ca_q = ['Q♠','Q♥','Q♦','Q♣']
    if botca_1 or botca_2 == 'Q♠':
        if botca_1 == 'Q♠':
                botpt1 += 0

        elif botca_2 == 'Q♠':
                botpt2 += 0
        
    if botca_1 or botca_2 == 'Q♥':
        if botca_1 == 'Q♥':
                botpt1 += 0

        elif botca_2 == 'Q♥':
                botpt2 += 0
        
    if botca_1 or botca_2 == 'Q♦':
        if botca_1 == 'Q♦':
                botpt1 += 0
            
        elif botca_2 == 'Q♦':
                botpt2 += 0
        
    if botca_1 or botca_2 == 'Q♣':
        if botca_1 == 'Q♣':
                botpt1 += 0

        elif botca_2 == 'Q♣':
                botpt2 += 0
        # ca_k = ['K♠','K♥','K♦','K♣']
    if botca_1 or botca_2 == 'K♠':
        if botca_1 == 'K♠':
                botpt1 += 0

        elif botca_2 == 'K♠':
                botpt2 += 0
        
    if botca_1 or botca_2 == 'K♥':
        if botca_1 == 'K♥':
                botpt1 += 0
            
        elif botca_2 == 'K♥':
                botpt2 += 0
        
    if botca_1 or botca_2 == 'K♦':
        if botca_1 == 'K♦':
                botpt1 += 0
            
        elif botca_2 == 'K♦':
                botpt2 += 0
                
    if botca_1 or botca_2 == 'K♣':
        if botca_1 == 'K♣':
                botpt1 += 0
                
        elif botca_2 == 'K♣':
                botpt2 += 0
                
    time.sleep(1.5)
    botpt = (botpt1 + botpt2)
while botpt >= 10 and botpt <= 20:
    botpt -= 10
    break
print('----------------------------')
#gamerule
#playerpoint with botpoint
while playerpt != botpt:
    #pok
    if playerpt1 and playerpt2 == 9:
        print('You Win!')
        print('Pok9')
        print('Bot point is: ',botpt)
        break

    elif playerpt1 and playerpt2 == 8:
        print('You Win!')
        print('Pok8')
        print('Bot point is: ',botpt)
        break

    elif botpt1 and botpt2 == 9:
        print('You Lose!')
        print('Bot got Pok9')
        print('Bot point is: ',botpt)
        break

    elif botpt1 and botpt2 == 8:
        print('You Lose!')
        print('Bot got Pok8')
        print('Bot point is: ',botpt)
        break

    elif playerpt > botpt:
        print('You Win!')
        print('Bot point is: ',botpt)
        break

    elif playerpt < botpt:
        print('You Lose!')
        print('Bot point is: ',botpt)
        break
    
    elif playerpt == botpt:
        print('Draw!')
        print('Bot point is: ',botpt)
        break
    break
print('Bot Cards is: ',botca_1, "," ,botca_2)
