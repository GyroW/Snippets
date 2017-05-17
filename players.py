ballingame = 1
maxballs = 5
maxplayers = 0
playeringame = 0
Gameover = True
Shootagain = 1

def startknop():
    global maxplayers
    global Gameover
    global playeringame
    if maxplayers == 0:
        Gameover = False
        playeringame = 1
    if ballingame == 1:
        maxplayers += 1
    if maxplayers > 4:
        maxplayers = 4


def outhole():
    global ballingame
    global playeringame
    if Gameover == False:    
        if Shootagain == 1:     #If false
            playeringame += 1   #Add to playeringame
        if playeringame > maxplayers:
            playeringame = 1
            ballingame += 1     #If we exceed maximum amount of players, go to next ball
        if ballingame > maxballs: #If we exceed maximum amount of balls, gameover
            gameover()

def gameover():
    global Gameover
    global ballingame
    global maxplayers
    Gameover = True
    ballingame = 1
    maxplayers = 0

while 1:
    var = input()
    if var == "a":
        startknop()
    elif var == "b":
        outhole()
    print("ballingame", ballingame )
    print("playeringame", playeringame)
    print("maxplayers", maxplayers)
    print("Gameover", Gameover)
    

