import os
import sys
import random
import time

def clear():
    os.system("clear")

clear() # clear before playing

play = input("Wanna play Blackjack. (y/n) : ")

if play == "y":
    # card 1-9 jack:10 queen:11 king:12 ace:13
    playerHand = []
    aiHand = []
    playerHand.append(random.randint(1,13))
    playerHand.append(random.randint(1,13))
    aiHand.append(random.randint(1,13))
    aiHand.append(random.randint(1,13))
    print("Ok nice! But aces are worth 1 ok.")
    playerHandWords = []
    for i in range(len(playerHand)):
        if 1 <= playerHand[i] <= 9:
            playerHandWords.append(str(playerHand[i]))
        elif playerHand[i] == 10:
            playerHandWords.append("Jack")
        elif playerHand[i] == 11:
            playerHandWords.append("Queen")
        elif playerHand[i] == 12:
            playerHandWords.append("King")
        elif playerHand[i] == 13:
            playerHandWords.append("Ace")
        else:
            print("An Oopsie happened!\nrandom did not give a valid value!???")
            sys.exit()
    aiHandWords = []
    for i in range(len(aiHand)):
        if 1 <= aiHand[i] <= 9:
            aiHandWords.append(str(aiHand[i]))
        elif aiHand[i] == 10:
            aiHandWords.append("Jack")
        elif aiHand[i] == 11:
            aiHandWords.append("Queen")
        elif aiHand[i] == 12:
            aiHandWords.append("King")
        elif aiHand[i] == 13:
            aiHandWords.append("Ace")
        else:
            print("error random did not give a valid value just try again it'll probably work next time" + str(aiHand))
            sys.exit()

    print("Your hand is a " + playerHandWords[0] + " and a " + playerHandWords[1] + ".")
    print("The Robot's hand is a " + aiHandWords[0] + " and a " + aiHandWords[1] + ".")
    def turn():
        playerChoice = input("Pull another card or keep your current hand (p/k) : ")
    
        if playerChoice == "p":
            playerHand.append(random.randint(1,13))
        
            playerHandWords = []
            for i in range(len(playerHand)):
                if 1 <= playerHand[i] <= 9:
                    playerHandWords.append(str(playerHand[i]))
                elif playerHand[i] == 10:
                    playerHandWords.append("Jack")
                elif playerHand[i] == 11:
                    playerHandWords.append("Queen")
                elif playerHand[i] == 12:
                    playerHandWords.append("King")
                elif playerHand[i] == 13:
                    playerHandWords.append("Ace")
                else:
                    print("An Oopsie happened!\nrandom did not give a valid value!???")
                    sys.exit()


            convertedNumbers = []
            for i in range(len(playerHand)):
                if playerHand[i] > 10 and playerHand[i] != 13:
                    convertedNumbers.append(10)
                elif playerHandWords[i] == "Ace":
                    convertedNumbers.append(1)
                else:
                    convertedNumbers.append(playerHand[i])
            total = 0
            for i in range(len(playerHand)):
                total += convertedNumbers[i]
            playerHandString = ", ".join(playerHandWords)
            if total > 21:
                print(str(total) + " is too much. You lose. (your deck was " + playerHandString + ")")
                sys.exit()
            elif total == 21:
                print("Wait you got 21! Aw man. You win.")
                sys.exit()
            else:
                print("Your total is " + str(total) + " and your deck is " + playerHandString + ".")
            convertedAiNumbers = []
            for i in range(len(aiHand)):
                if aiHand[i] > 10 and aiHand[i] != 13:
                    convertedAiNumbers.append(10)
                elif aiHand[i] == 13:
                    convertedAiNumbers.append(1)
                else:
                    convertedAiNumbers.append(aiHand[i])
            totalAi = 0
            for i in range(len(aiHand)):
                totalAi += convertedAiNumbers[i]
            aiHandWords = []
            for i in range(len(aiHand)):
                if 1 <= aiHand[i] <= 9:
                    aiHandWords.append(str(aiHand[i]))
                elif aiHand[i] == 10:
                    aiHandWords.append("Jack")
                elif aiHand[i] == 11:
                    aiHandWords.append("Queen")
                elif aiHand[i] == 12:
                    aiHandWords.append("King")
                elif aiHand[i] == 13:
                    aiHandWords.append("Ace")
                else:
                    print("An Oopsie happened!\nrandom did not give a valid value!???")
                    sys.exit()
            aiHandString = ", ".join(aiHandWords)
            if totalAi > 21:
                print("I got " + str(totalAi) + ". You win. Aw man.")
                sys.exit()
            elif total == 21:
                print("I got 21! Haha you loossee.")
                sys.exit()
            else:
                print("The robot's total is " + str(totalAi) + ". And the robot's deck is " + aiHandString)

            return 1
        elif playerChoice == "k":
            print("Ok. Looks like your standing.")
            return 0
    def aiTurn():
        aiChoice = "k"

        convertedAiNumbers = []
        for i in range(len(aiHand)):
            if aiHand[i] > 10 and aiHand[i] != 13:
                convertedAiNumbers.append(10)
            elif aiHand[i] == 13:
                convertedAiNumbers.append(1)
            else:
                convertedAiNumbers.append(aiHand[i])
        totalAi = 0
        for i in range(len(aiHand)):
            totalAi += convertedAiNumbers[i]

        convertedNumbers = []
        for i in range(len(playerHand)):
            if playerHand[i] > 10 and playerHand[i] != 13:
                convertedNumbers.append(10)
            elif playerHand[i] == 13:
                convertedNumbers.append(1)
            else:
                convertedNumbers.append(playerHand[i])
        total = 0
        for i in range(len(playerHand)):
            total += convertedNumbers[i]

        
        # total : pull chance 2:100% 3:100% 4:100% 5:100% 6:100% 7:90% 8:90% 9:90% 10:90% 11:90% 12:80% 13:80% 14:70% 15:60% 16:40% 17:30% 18:10% 19:5% 20:0%
        # if 22 > player > ai. ai always pulls
        
        choiceMaker = random.randint(1,20)

        if totalAi < total < 22:
            aiChoice = "p"
        elif 1 < totalAi < 7:
            aiChoice = "p"
        elif 6 < totalAi < 12:
            if choiceMaker > 2:
                aiChoice = "p"
            else:
                aiChoice = "k"
        elif 11 < totalAi < 14:
            if choiceMaker > 4:
                aiChoice = "p"
            else:
                aiChoice = "k"
        elif totalAi == 14:
            if choiceMaker > 6:
                aiChoice = "p"
            else:
                aiChoice = "k"
        elif totalAi == 15:
            if choiceMaker > 8:
                aiChoice = "p"
            else:
                aiChoice = "k"
        elif totalAi == 16:
            if choiceMaker > 12:
                aiChoice = "p"
            else:
                aiChoice = "k"
        elif totalAi == 17:
            if choiceMaker > 14:
                aiChoice = "p"
            else:
                aiChoice = "k"
        elif totalAi == 18:
            if choiceMaker > 18:
                aiChoice = "p"
            else:
                aiChoice = "k"
        elif totalAi == 19:
            if choiceMaker > 19:
                aiChoice = "p"
            else:
                aiChoice = "k"
        elif totalAi == 20:
            aiChoice = "k"
        else:
            print("ummmm the ai broke!!!??????")

    
        if aiChoice == "p":
            aiHand.append(random.randint(1,13))
            
            print("The Robot decided to pull")

            aiHandWords = []
            for i in range(len(aiHand)):
                if 1 <= aiHand[i] <= 9:
                    aiHandWords.append(str(aiHand[i]))
                elif aiHand[i] == 10:
                    aiHandWords.append("Jack")
                elif aiHand[i] == 11:
                    aiHandWords.append("Queen")
                elif aiHand[i] == 12:
                    aiHandWords.append("King")
                elif aiHand[i] == 13:
                    aiHandWords.append("Ace")
                else:
                    print("An Oopsie happened!\nrandom did not give a valid value!???")
                    sys.exit()


            convertedAiNumbers = []
            for i in range(len(aiHand)):
                if aiHand[i] > 10 and aiHand[i] != 13:
                    convertedAiNumbers.append(10)
                elif aiHand[i] == 13:
                    convertedAiNumbers.append(1)
                else:
                    convertedAiNumbers.append(aiHand[i])
            totalAi = 0
            for i in range(len(aiHand)):
                totalAi += convertedAiNumbers[i]
            aiHandString = ", ".join(aiHandWords)
            if totalAi > 21:
                print("I got " + str(totalAi) + ". You win. Aw man.")
                sys.exit()
            elif totalAi == 21:
                print("I got 21! Haha you loossee.")
                sys.exit()
            else:
                print("The robot's total is " + str(totalAi) + ". And the robot's deck is " + aiHandString)
            return 1
        elif aiChoice == "k":
            print("The robot has decided to stand.")
            return 0

            
    while True:
        turn()
        time.sleep(1)
        aiTurn()



elif play == "n":
    print("ok bye!")
    sys.exit()
else:
    print("invalid input")

