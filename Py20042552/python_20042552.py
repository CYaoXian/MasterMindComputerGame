#Importing random
import random

#This function is to start the game and welcome player 
def game_Start(): 
    print('\n.................................................................')
    print('|                Welcome to Master Mind Computer Game!          |')
    print('|                    By Chua Yao Xian (20042552)                |')
    print('.................................................................')
    print(' ')

    start = input("Enter 'P' to start the Master Mind Computer Game: ").upper()
    if start == 'P':
        instruction()

    else:
        print("ERROR INCORRECT SELECTION, You can only enter 'P' or 'p'")
        game_Start()
        
      
#This function is to show the instruction of master mind computer game      
def instruction():
    print('\n***How To Play***')
    print('1. You are required to guess 4 colour code that in my mind.')
    print('2. You are required to input the first letter of your colour choices. Example: Blue = B')
    print('3. You are required to select 4 out of 6 colours from the given colour list.')
    print('4. The colour choices are: ')
    print('   -(B)lue, (P)ink, (R)ed, (O)range, (G)reen, (Y)ellow')
    print('5. You can select the same colours more than once.')
    print('6. You have a total of 10 tries to guess the colour code.')
    print('7. If you input the correct sequence of the colour code then, YOU ARE A MASTERMIND!!')
    print('GoodLuck!! Enjoy the game!!')
    print(' ')
    mastermind_Codes()
   
            
#This function is to start the code
def mastermind_Codes():
    #List of colour available
    colour_List = ['B', 'P', 'R', 'O', 'G', 'Y']
    print('***The game start***')
    print('Colour list = (B)lue,(P)ink,(R)ed,(O)range,(G)reen,(Y)ellow')
    print('Choose 4 colour out of 6 from the colour list in simple form!! Example: BPRO')
    tries = 0
    mastermind_Codes = True

    
    while mastermind_Codes:
        random_ColourList = random.sample(colour_List, 4)
        
        #The line below is the master mind game answer and it will not show in the real game
        print(random_ColourList)
        print('Above the list it will not show in the real game, JUST A DEMO')
    
        while mastermind_Codes:
            colourCode_Correct = 0
            colour_Guess = 0
            playerGuess_2 = []
            colour_Code = []
          
            #Prompt player to enter their colour code guess
            player_Guess = input('\nPlease enter 4 colour code from colour list: ').upper()
            tries = tries + 1
            

            #The line below is to determine weather player enter 4 colour code
            if len(player_Guess) != len(random_ColourList):
                print('\nERROR INCORRECT COLOUR CODE, Please enter only 4 colour code from colour list :)')
                continue

            #The line below is to determine weather player enter colour code exist
            for u in range(4):
                if player_Guess[u] not in colour_List:
                    print('\nERROR INCORRECT COLOUR CODE, The colour code you entered does not match colour list :(')
                    break

                
            #The line below is for determine correct colour code place
            for u in range(4):
                if player_Guess[u] == random_ColourList[u]:
                    colourCode_Correct = colourCode_Correct + 1

            #The line below is for determine wrong colour code place
            for u in range(4):
                if player_Guess[u] in random_ColourList and player_Guess[u] != random_ColourList[u]:

                    playerGuess_2.append(player_Guess[u])
                    colour_Code.append(random_ColourList[u])


            for u in range(len(colour_Code)):
                if playerGuess_2[u] in colour_Code and player_Guess[u] != playerGuess_2[u]:
                    colour_Guess = colour_Guess + 1

                    
            #This is when user wins
            if colourCode_Correct == 4:
                print('\nCongratulation!! YOU ARE A MASTERMIND!! ^o^')
                print('You had took', tries, 'tries to be MASTERMIND!! ^O^')
                print('The correct answer is ', random_ColourList)
                mastermind_Code = False
                game_Repeat()

            else:
                print('Correct colour in right place:', colourCode_Correct)
                print('Correct colour but wrong place:', colour_Guess)

            #This show the answer when there are too many tries and End Game
            if (tries >= 1 and tries <= 10) and (colourCode_Correct != 4):
                print('Number of tries:', tries)
                print('\nPlease Try Again !!')

            if tries == 10:
                print('-------------------------------------------')
                print('/                Game Over!!!             /')
                print('-------------------------------------------')
                print('You have reached the maximum number of tries \nThe correct answer is: ', random_ColourList)
                mastermind_Code = False
                game_Repeat()

                
#This function is ask player weather they want to play again
def game_Repeat():
    repeat_Game = input('\nDo you want to play again? (Y/N): ').upper()
    if repeat_Game == 'Y':
        print('\n ****************************NEW GAME****************************')
        game_Start()

    if repeat_Game == 'N':
        print('The Program Ended. Thank For Playing The Master Mind Computer Game!!!!')
        quit()

    elif repeat_Game != 'Y' or repeat_Game != 'N':
        print("ERROR INCORRECT SELECTION, You can only enter 'Y' or 'N'")
        game_Repeat()

game_Start()          

    
