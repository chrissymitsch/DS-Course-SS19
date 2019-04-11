# Exercise 2
while True:
    print("Let's play Tic Tac Toe!")

    finished = False
    ready1 = 'n'
    ready2 = 'n'
    x = " X "
    o = " O "
    currentStatus = ["(1)","(2)","(3)","(4)","(5)","(6)","(7)","(8)","(9)"]
    taken = [False,False,False,False,False,False,False,False,False]


    def showGameStatus():
        print(" " + currentStatus[0] + " | " + currentStatus[1] + " | " + currentStatus[2] + " ")
        print(" " + currentStatus[3] + " | " + currentStatus[4] + " | " + currentStatus[5] + " ")
        print(" " + currentStatus[6] + " | " + currentStatus[7] + " | " + currentStatus[8] + " \n")


    def turn(p, player):
        print("Choose a location of" + p)
        showGameStatus()
        
        while True:
            try:
                location = int(input("Player " + player + ":" + p + "--> ")) - 1
                break
            except ValueError:
                continue
            
        while taken[location]:
            # Already taken
            location = int(input("CHOOSE ANOTHER:" + p + "--> ")) - 1
        currentStatus[location] = p
        taken[location] = True

        showGameStatus()

    
    def winner(p):
        # define different winning combinations
        # horizontal
        if (currentStatus[0] == p and currentStatus[1] == p and currentStatus[2] == p):
            return True
        if (currentStatus[3] == p and currentStatus[4] == p and currentStatus[5] == p):
            return True
        if (currentStatus[6] == p and currentStatus[7] == p and currentStatus[8] == p):
            return True
            
        #vertical
        if (currentStatus[0] == p and currentStatus[3] == p and currentStatus[6] == p):
            return True
        if (currentStatus[1] == p and currentStatus[4] == p and currentStatus[7] == p):
            return True
        if (currentStatus[2] == p and currentStatus[5] == p and currentStatus[8] == p):
            return True
            
        #diagonal
        if (currentStatus[0] == p and currentStatus[4] == p and currentStatus[8] == p):
            return True
        if (currentStatus[2] == p and currentStatus[4] == p and currentStatus[6] == p):
            return True


    def draw():
        # if everything is taken
        return taken[0] and taken[1] and taken[2] and taken[3] and taken[4] and taken[5] and taken[6] and taken[7] and taken[8]


    def finished():
        playerOneWinner = winner(x)
        playerTwoWinner = winner(o)
        finished = playerOneWinner or playerTwoWinner
    
        if playerOneWinner:
            print("***************************")
            print("* PLAYER ONE WON THE GAME *")
            print("***************************\n")
            return True
            
        if playerTwoWinner:
            print("***************************")
            print("* PLAYER TWO WON THE GAME *")
            print("***************************\n")
            return True
            
        if draw():
            print("* Nobody won *\n")
            finished = True
            return True
            
        return False


    # THE GAME
    while not (finished()):
        # Player One
        while (ready1 != 'y'):
            print("Ready, Player One? (y/n)")
            ready1 = input()
    
        if ready1 == 'y':
            # Player One's turn
            turn(x, "One")

            if (finished()):
                break
           
        # Player Two
        while (ready2 != 'y'):
            print("Ready, Player Two? (y/n)")
            ready2 = input()
    
        if ready2 == 'y':
            # Player Two's turn
            turn(o, "Two")


    # PLAY AGAIN QUESTION
    while True:
        again = input("Play again? (y/n) ")
        if again == 'y' or again == 'n':
            break

    if again == 'y':
        print("Cool!")
        continue
    else:
        print("Have a nice day!")
        break
