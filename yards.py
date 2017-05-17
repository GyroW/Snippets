DictSingleyards = {'yard1': 0, 'yard2': 0, 'yard3': 0, 'yard4': 0, 'yard5': 0, 'yard6': 0, 'yard7': 0, 'yard8': 0, 'yard9' :0, 'yard10': 0} #1 -10
DictDecayards = {'yardsleft': 0, 'yards10': 0, 'yards20': 0, 'yards30': 0, 'yards40': 0, 'yards50': 0, 'yards-40': 0, 'yards-30': 0, 'yards-20': 0, 'yards-10': 0, 'yardsright': 0} #Left, 10, 20, 30, 40, 50, -40, -30, -20, -10, Right
DictGoalscores = {'5000': 0, 'extra ball': 0, 'special': 0}
DictLTDscores = {'goal': 0, 'special': 0}
DictBonus = {'1000': 0, '2000': 0, '3000': 0, '4000': 0, '5000': 0, '6000': 0, '7000': 0, '8000': 0, '9000': 0, '10000': 0}
DictPijltjes = {'left': 0, 'right': 0}
Dict30yardswlit = {'1': 0, '2': 0, '3': 0, '4': 0}

IndexSingleyards = ['yard1', 'yard2', 'yard3', 'yard4', 'yard5', 'yard6', 'yard7', 'yard8', 'yard9', 'yard10']
IndexDecayards = ['yardsleft', 'yards10', 'yards20', 'yards30', 'yards40', 'yards50', 'yards-40', 'yards-30', 'yards-20', 'yards-10', 'yardsright']
yardsvalue = 0
decayardsvalue = 0
yardsdirection = True #Right
def yards(amount):
    global DictSingleyards
    global DictDecayards
    global yardsvalue
    global decayardsvalue
    if yardsdirection: 
        yardsvalue +=  amount
    else:
        yardsvalue -=  amount
    while yardsvalue > 10:
        decayardsvalue += 1
        yardsvalue -= 10
    while yardsvalue < 0:
        decayardsvalue -= 1
        yardsvalue += 10
    if decayardsvalue < 0 and yardsvalue < 0:
        decayardsvalue = 0
        yardsvalue = 0
    if decayardsvalue > 11:
        goal()
        decayardsvalue = 0
        yardsvalue = 0
#######################
#Lights
#######################
    for i in range(0, len(IndexSingleyards)):               #Resets dictionary to default state (all 0s)
        DictSingleyards[IndexSingleyards[i]] = 0
    for i in range(0, len(IndexDecayards)):
        DictDecayards[IndexDecayards[i]] = 0
    DictSingleyards[IndexSingleyards[yardsvalue - 1]] = 1   #Sets appropriate value (depending on yardvalue) to 1 -> this lite will be on
    DictDecayards[IndexDecayards[decayardsvalue]] = 1       #Sets appropriate value (depending on decayardvalue) to 1 -> this lite will be on










