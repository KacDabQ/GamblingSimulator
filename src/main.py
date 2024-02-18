import random, time

def changeWallet(w, amountToChange, s):
    w = int(w) + amountToChange
    walletUpdate = open(s['Wallet'], 'w')
    walletUpdate.write(str(w)) # Saving wallet
    walletUpdate.close()

def main():
    print('WELCOME TO GAMBLING SIMULATOR v0.2.1')
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
            print('crime, double, help, lottery, roullete, wallet, work')
        


        elif command == 'work':
            moneyAmount = random.randint(2,7)
            changeWallet(wallet, moneyAmount, storages)
            print('You have earned', str(moneyAmount) + '$!')
        


        elif command == 'wallet':
            print('You have:', wallet, '$!')
        


        elif command == 'crime':
            crimeSuccess = random.randint(1,3)
            if crimeSuccess >= 2:
                moneyAmount = random.randint(10,150)
                changeWallet(wallet, moneyAmount, storages)
                print('You are a bad person. You have earned:', str(moneyAmount) + '$!')
            else:
                moneyAmount = random.randint(30,250)
                changeWallet(wallet, moneyAmount * -1, storages)
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
                changeWallet(wallet, bet * -1, storages)
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
                        changeWallet(wallet, int(winnings), storages)
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
                changeWallet(wallet, int(winnings), storages)
            elif didYouWin == 0 and wallet - bet >= 0 and bet >= 5 and wallet >= 0:
                print('You lose.')
                changeWallet(wallet, int(bet) * -1, storages)
            else:
                print('You either have bet too small amount of $, or you are too poor.')
        


        elif command == 'lottery':
            goodNumbers = True
            winValue = 0
            bet = int(input('Buy a lottery ticket (at least 5$): '))
            chosenNumbersNON = input('Pick 3 numbers from 1 to 10 (including both ends) (after a space): ')
            chosenNumbersBRKN = list(chosenNumbersNON.split(" ")) 
            chosenNumbers = []
            for number in chosenNumbersBRKN: # INT Every number
                chosenNumbers.append(int(number))
            for number in chosenNumbers:
                if number <= 0 or number >= 11:
                    goodNumbers = False
            winningNumbers = []
            repeat = 3
            while repeat > 0:
                winningNumbers.append(random.randint(1,10))
                repeat -= 1
            if wallet - bet >= 0 and bet >= 5 and wallet >= 0 and goodNumbers == True and len(chosenNumbers) == 3:
                changeWallet(wallet, bet * -1, storages)
                if chosenNumbers[0] == winningNumbers[0]:
                    winValue += 1
                if chosenNumbers[1] == winningNumbers[1]:
                    winValue += 1
                if chosenNumbers[2] == winningNumbers[2]:
                    winValue += 1
                time.sleep(random.randint(2,4))
                print(winningNumbers)
                if winValue == 1:
                    winnings = bet * 4
                    winnings = round(winnings, 0)
                    print('You guessed 1 number!')
                    print('You have earned', int(winnings), '$!')
                    changeWallet(wallet, int(winnings), storages)
                elif winValue == 2:
                    winnings = bet * 60
                    winnings = round(winnings, 0)
                    print('You guessed 2 numbers!!!')
                    print('You have earned', int(winnings), '$!')
                    changeWallet(wallet, int(winnings), storages)
                elif winValue == 3:
                    winnings = bet * 800
                    winnings = round(winnings, 0)
                    print('JACKPOT!!!') # Jackpot
                    print('You have earned', int(winnings), '$!')
                    changeWallet(wallet, int(winnings), storages)
                else:
                    print('You lost')
                    walletUpdate = open(storages['Wallet'], 'w')
                    walletUpdate.write(str(wallet))
                    walletUpdate.close()
            else:
                print('You either have bet too small amount of $, or you are too poor, OR you have picked a wrong number or the amount of them.')

# Call main() if this is the main execution modul
if __name__ == '__main__':
    main()