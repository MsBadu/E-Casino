# Introduce Games and welcome player
print("Welcome to E's Casino.")
print('You have a budget of $500')
# Create a function that list all games the user can play
def showFunctionsMenu():
    print('Game 1: Number Guess Games')
    print('Game 2: Craps')
    print('Game 3: Zambales')
    print('Game 4: Cho-HAn')
    print('Game 5: Quit')
    return int(input('What game would you like to play first (only enter the number): '))

# Import random number
import random

# Number Guess Games
def numberGuess(betAmount):
    # Give a range between 0 to 100
    # Use random.randint(range) to play the roll of the dice
    randomNumber = random.randint(0, 100)
    # Provide the user with instructions
    print('Instructions: You have third tries to guess a number between 0 to 100.')
    # Give three inputs that have the user guess the right number
    firstTry = int(input('Please guess a number between 0 - 100: '))
    # Have each try equal the generated random number
    if firstTry == randomNumber:
        print('Congrats, you guess the right number on the first try!!')
        tripleMoneyBet = betAmount * 3
        # print ('Payout: ' + str(tripleMoneyBet))
        return tripleMoneyBet
    else:
        # Define second variable after the else statement
        secondTry = int(input('Try again: '))
        if secondTry == randomNumber:
            print('Second time is the charm you got it!')
            doubleMoneyBet = betAmount * 2
            # print ('Payout: ' + str(doubleMoneyBet))
            return doubleMoneyBet
        else:
            thirdTry = int(input('Try again: '))
            if thirdTry == randomNumber:
                print('Third time is the charm you got it!')
                sameMoneyBet = betAmount * 1
                # print('Payout: ' + str(sameMoneyBet))
                return sameMoneyBet
            else:
                print('Sorry, you are out of guesses :(')
                print('The random number was: ' + str(randomNumber))
                NoBetNumber = betAmount * 0
                # print('Payout: ' + str(NoBetNumber))
                return NoBetNumber

# Craps
def Craps(betAmount):
    # crapsBet = int(input('How much money would you like to bet: '))
    print('Instructions: The goal is to roll a 7, 11, or match your point to win. Be aware if you roll a 2,3 or 12 you will lose')
    # Have the range go from 1 to 6 as a real dice has six sides
    diceOne = random.randint(1,6)
    diceTwo = random.randint(1,6)
    diceTotal = diceOne + diceTwo
    # State that user wins if they get a 7 or 11
    if diceTotal == 7 or diceTotal == 11:
        print('You won!!')
        print ('You rolled a ' + str(diceTotal))
        doubleMoneyBet = betAmount * 2
        print('Payout: ' + str(doubleMoneyBet))
        return doubleMoneyBet
    # lose 2,3, or 12
    else:
        if diceTotal == 2 or diceTotal == 3 or diceTotal == 12:
            print('Sorry you got a ' + str(diceTotal) + '.' + ' You lost')
            noMoneyBet = betAmount * 0
            print('Payout: ' + str(noMoneyBet))
            return noMoneyBet
        # Otherwise shoot for point
        else:
            print('You need to roll a ' + str(diceTotal))
            # Set point
            while True:
                shootingDiceOne = random.randint(1, 6)
                shootingDiceTwo = random.randint(1, 6)
                shootingDiceTotal = shootingDiceTwo + shootingDiceOne
                # Let player roll
                print('You rolled a: ' + str(shootingDiceTotal))
                # Win: Match point
                if shootingDiceTotal == diceTotal:
                    print('You won!!')
                    doubleMoneyBet = betAmount * 2
                    print('Payout: ' + str(doubleMoneyBet))
                    return doubleMoneyBet
                    # break
                # Lose: roll a 7
                else:
                    if shootingDiceTotal == 7:
                        print('You lost. You rolled a 7')
                        noMoneyBet = betAmount * 0
                        print('Payout: ' + str(noMoneyBet))
                        return noMoneyBet
                        # break
                    # anything else roll again
                    else:
                        print('Roll again')

# Zambales
def Zambales(betAmount):
    print('Instruction: You have five tries to roll the same number on both dices.')
    counter = 0
    # Use a while True loop
    while True:
        DiceOne = random.randint(1, 6)
        DiceTwo = random.randint(1, 6)
        counter += 1
        # print('Counter ' + str(counter))
        # Let player roll
        # Win if the dices equal each other
        if DiceOne == DiceTwo:
            print('You won')
            # If user guesses the right number on the first two tries double their bet
            if counter < 3:
                # Double their bet if they win on the first two try
                doubleMoneyBet = betAmount * 2
                print('Attempt: ' + str(counter))
                print ('You rolled a ' + str(DiceOne) + ' and ' + str(DiceTwo))
                print('Payout: ' + str(doubleMoneyBet))
                return doubleMoneyBet
            if counter >= 3:
                # Return what they bet on their 4 and 5 tries.
                sameMoneybet = betAmount * 1
                print('Attempt: ' + str(counter))
                print ('You rolled a ' + str(DiceOne) + ' and ' + str(DiceTwo))
                print('Payout: ' + str(sameMoneybet))
                return sameMoneybet
        # End game using else statement
        else:
            # Get five rolls total
            if counter == 5:
                print ('Attempt: ' + str(counter))
                print ('You rolled a ' + str(DiceOne) + ' and ' + str(DiceTwo))
                print('Sorry you are out of chances')
                noMoneyBet = betAmount * 0
                print('Payout: ' + str(noMoneyBet))
                return noMoneyBet
        # Create a program that show user what they rolled each time
        print('Attempt: ' + str(counter))
        print('You rolled a ' + str(DiceOne) + ' and ' + str(DiceTwo))


# Cho-HAn
def ChoHAn(betAmount):
    print('Instruction: You must guess if the total of both dices is an even or odd number.')
    # Get user bet
    # choHAnBet = int(input('How much money would you like to bet: '))
    # Ask user what their guess is
    choHAnUserGuess = input('Will the sum of the dice be Chō or Han (even or odd): ')
    # 2 random randint ranging from (1,6)
    choHAnDiceOne = random.randint(1, 6)
    choHAnDiceTwo = random.randint(1, 6)
    choHAnDiceTotal = choHAnDiceOne + choHAnDiceTwo
    # Create an if statement for if the number is gonna be even or odd
    if (choHAnDiceTotal % 2) == 0:
        # Provide an if statement for the various answer user could give
        if choHAnUserGuess == 'Even' or choHAnUserGuess == 'even' or \
                choHAnUserGuess == 'Chō' or choHAnUserGuess == 'chō' or choHAnUserGuess == 'cho' or choHAnUserGuess == 'Cho':
            print('You won.The dice total was ' + str(choHAnDiceTotal))
            doubleMoneyBet = betAmount * 2
            print('Payout: ' + str(doubleMoneyBet))
            return doubleMoneyBet
        else:
            # Use the else statement for if the user guess the wrong number
            print('You lost.The dice total was ' + str(choHAnDiceTotal))
            noMoneyBet = betAmount * 0
            print('Payout: ' + str(noMoneyBet))
            return noMoneyBet
    elif (choHAnDiceTotal % 2) == 1:
        if choHAnUserGuess == 'Odd' or choHAnUserGuess == 'odd' or choHAnUserGuess == 'Han' or choHAnUserGuess == 'han':
            print('You won.The dice total was ' + str(choHAnDiceTotal))
            doubleMoneyBet = betAmount * 2
            print('Payout: ' + str(doubleMoneyBet))
            return doubleMoneyBet
        else:
            print('You lose.The dice total was ' + str(choHAnDiceTotal))
            noMoneyBet = betAmount * 0
            print('Payout: ' + str(noMoneyBet))
            return noMoneyBet


# Create function that return wins to wallet
def getBet(startMoney):
    while True:
        # Step 1: Ask user for bet
        betAmount = int(input('Place a Bet: '))
        # Step 2: Check if bet is more than starting money
        if betAmount > startMoney:
            # Step 3: If bet is more .... tell them bad bet
            print('You have bet more money than you have in your account')
        else:
            # Step 4: If bet is less or equal ..... tell them good bet
            break
    return betAmount

# Create variable that explains the wallet has $500
startMoney = 500
while True:
    # Asking users which game they want to play
    # Have an if statement that ensure users still have money in their wallet
    if startMoney > 0:
        userChoice = showFunctionsMenu()
        if userChoice == 1:
            # Create a variable that saves the getBet function
            # Subtract/add how much user has bet with what in their wallet
            bettingFunction = getBet(startMoney)
            startMoney -= bettingFunction
            startMoney += numberGuess(bettingFunction)
            print('Your current budget is ' + str(startMoney))
            # Add a space for appearance
            print(' ')
        elif userChoice == 2:
            bettingFunction = getBet(startMoney)
            startMoney -= bettingFunction
            startMoney += Craps(bettingFunction)
            print('Your current budget is ' + str(startMoney))
            print(' ')
        elif userChoice == 3:
            bettingFunction = getBet(startMoney)
            startMoney -= bettingFunction
            startMoney += Zambales(bettingFunction)
            print('Your current budget is ' + str(startMoney))
            print(' ')
        elif userChoice == 4:
            bettingFunction = getBet(startMoney)
            startMoney -= bettingFunction
            startMoney += ChoHAn(bettingFunction)
            print('Your current budget is ' + str(startMoney))
            print(' ')
        elif userChoice == 5:
            print('Your total balance: ' + str(startMoney))
            print('Exit, Thank you for playing')
            break
    # Use else if they are out of money
    else:
        print('Exit; Sorry you can no longer play as you are out of money')
        break

















