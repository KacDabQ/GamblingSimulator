import random, time
print('WELCOME TO GAMBLING SIMULATOR v0.0.1')
storages = {'Wallet': './data/wallet.txt', 'Inventory': './data/inventory.txt'} # Paths
command = ''

def readWallet():
    walletLoad = open(storages['Wallet'], 'r')
    wlt = int(walletLoad.read())
    walletLoad.close()
    return wlt

def writeWallet(amount):
    walletUpdate = open(storages['Wallet'], 'w')
    walletUpdate.write(str(amount)) # Saving wallet
    walletUpdate.close()

while command != 'quit':
    wallet = readWallet()

    ### COMMANDS ###
    command = input('>> ')

    if command == 'help':
        print('roullete, wallet, work')
    
    elif command == 'work':
        moneyAmount = random.randint(5,20)
        wallet += moneyAmount
        writeWallet(wallet)
        print(f'You earned {moneyAmount}$!')
    
    elif command == 'wallet':
        print(f'You have {wallet}$!')

    elif command == 'roullete':
        lost = False
        goodNumbersRLT = True
        bet = int(input('Bet on a roullete (at least 5$)!: ').removesuffix("$"))
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
        if goodNumbersRLT and wallet >= bet and bet >= 5 and wallet >= 0: # Check for requirements
            wallet -= bet
            writeWallet(wallet)
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
                if number == drawANumberRLT and not lost:
                    winnings = bet * (36/len(chosenNumbers))
                    winnings = round(winnings, 0)
                    print('YOU WON!!!')
                    print(f'You have earned {winnings}$!')
                    wallet += int(winnings)
                    writeWallet(wallet)
                    break
        else:
            print('You either have bet too small amount of $, or you are too poor.')
