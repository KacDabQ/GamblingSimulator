import random
import time
print('WELCOME TO GAMBLING SIMULATOR v0.1.0')
storages = {'Wallet': './data/wallet.txt', 'Inventory': './data/inventory.txt'} # Paths
command = ''

while command != 'quit':

    ### WALLET SAVING ###
    walletLoad = open(storages['Wallet'], 'r')
    wallet = int(walletLoad.read())
    walletLoad.close()

    ### COMMANDS ###
    command = input('>> ')

    if command == 'help':
        print('roullete, wallet, work')
    
    elif command == 'work':
        moneyAmount = random.randint(2,7)
        wallet = int(wallet) + moneyAmount
        walletUpdate = open(storages['Wallet'], 'w')
        walletUpdate.write(str(wallet)) # Saving wallet
        walletUpdate.close()
        print('You have earned', str(moneyAmount) + '$!')
    
    elif command == 'wallet':
        print('You have:', wallet, '$!')
    
    elif command == 'crime':
        crimeSuccess = random.randint(1,3)
        if crimeSuccess >= 2:
            moneyAmount = random.randint(10,150)
            wallet = int(wallet) + moneyAmount
            walletUpdate = open(storages['Wallet'], 'w')
            walletUpdate.write(str(wallet)) # Saving wallet
            walletUpdate.close()
            print('You are a bad person. You have earned:', str(moneyAmount) + '$!')
        else:
            moneyAmount = random.randint(30,250)
            wallet = int(wallet) - moneyAmount
            walletUpdate = open(storages['Wallet'], 'w')
            walletUpdate.write(str(wallet)) # Saving wallet
            walletUpdate.close()
            print('BUSTED! YOU HAVE LOST:', str(moneyAmount) + '$!')

    ### GAMBLING COMMANDS ###
    elif command == 'roullete':
        lost = False
        goodNumbersRLT = True
        bet = int(input('Bet on a roullete (at least 5$)!: '))
        chosenNumbersNON = input('PICK A NUMBER FROM 1 TO 36 (add new numbers after space): ')
        chosenNumbersBRKN = list(chosenNumbersNON.split(" ")) 
        chosenNumbers = []
        for number in chosenNumbersBRKN: # INT Every number
            chosenNumbers.append(int(number))
        for number in chosenNumbers:
            if number <= 0 or number >= 37: # Check for good numbers
                print('You picked numbers out of range :/')
                goodNumbersRLT = False
                break
        if goodNumbersRLT == True and wallet - bet >= 0 and bet >= 5 and wallet >= 0: # Check for requirements
            wallet = wallet - bet
            walletUpdate = open(storages['Wallet'], 'w')
            walletUpdate.write(str(wallet))
            walletUpdate.close()
            print('Remember! If 0 will drop, youll lose your bet! Casino also need money :(')
            drawANumberRLT = random.randint(0,36)
            time.sleep(1)
            print('The numbers are rolling in...')
            time.sleep(random.randint(3,7))
            print('The number is:', drawANumberRLT)
            if drawANumberRLT == 0:
                print('Bad Luck :/')
                lost = True
            for number in chosenNumbers: # Did you win?
                if number == drawANumberRLT and lost == False:
                    winnings = bet * (36/len(chosenNumbers))
                    winnings = round(winnings, 0)
                    print('YOU WON!!!')
                    print('You have earned', int(winnings), '$!')
                    wallet = wallet + int(winnings)
                    walletUpdate = open(storages['Wallet'], 'w')
                    walletUpdate.write(str(wallet))
                    walletUpdate.close()
                    break
        else:
            print('You either have bet too small amount of $, or you are too poor.')

    elif command == 'double':
        didYouWin = random.randint(0,1)
        bet = int(input('Tell us your bet: '))
        time.sleep(random.randint(2,4))
        if didYouWin == 1 and wallet - bet >= 0 and bet >= 5 and wallet >= 0:
            wallet = wallet - int(bet)
            winnings = bet * 2
            winnings = round(winnings, 0)
            print('YOU WON!!!')
            print('You have earned', int(winnings), '$!')
            wallet = wallet + int(winnings)
            walletUpdate = open(storages['Wallet'], 'w')
            walletUpdate.write(str(wallet))
            walletUpdate.close()
        elif didYouWin == 0 and wallet - bet >= 0 and bet >= 5 and wallet >= 0:
            print('You lose.')
            wallet = wallet - int(bet)
            walletUpdate = open(storages['Wallet'], 'w')
            walletUpdate.write(str(wallet))
            walletUpdate.close()
        else:
            print('You either have bet too small amount of $, or you are too poor.')