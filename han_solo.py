planets = ['Tatooine', 'Naboo', 'Hoth', 'Devaron', 'Dantooine', 'Alderaan']

hyperTable = [[-1, 40 , 20 ,150 ,130, 218],
              [40, -1, 135, 70, 45, 198],
              [20, 135, -1, 20, 60, 166],
              [150, 70, 20, -1, 112, 62],
              [130, 45, 60, 112, -1, 15],
              [218, 198, 166, 62, 15, -1]]

def getPlanetIndex(planets, name):
    for i in range(len(planets)):
        if planets[i] == name:
            return i
        
def getPlanetName(planets, index):
    for i in range(len(planets)):
        if i == index:
            return planets[i]

def getMinEnergyTargetPlanet(table, planets, name):
    row = getPlanetIndex(planets, name)
    minDistance = float('inf')
    current = None
    for i in range(len(table[row])):
        if table[row][i] < minDistance and table[row][i] > 0 :
            minDistance = table[row][i]
            current = getPlanetName(planets, i)
    return current



def getAllPossibleJumps(planets, sourceID, energyConsumed):
    planetsArray = []
    energy = []
    for i in range(len(planets)):
        if i != sourceID:
            planetsArray.append(planets[i])
            energy.append((hyperTable[sourceID][i]) + energyConsumed)
    planetsArray.append(planets[sourceID])
    energy.append(energyConsumed)
    return planetsArray, energy

def printJumps(planetsArray , energy):
    # planetsArray , energy = all
    print('jumps:')
    for i in range(len(planetsArray)-1):
        print(f"{planetsArray[i]} via {planetsArray[len(planetsArray)-1]} for {energy[i-2].energyConsumed}")
  
class Jump:
    def __init__(self, sourceId, targetID, energyConsumed):
        self.sourceID = sourceId
        self.targetID = targetID
        self.energyConsumed = energyConsumed

def getMinEnergyJump(jumps):
    min = float('inf')
    selected = None
    for i in range(len(jumps)):
        if jumps[i].energyConsumed < min:
            min = jumps[i].energyConsumed
            selected = jumps[i]
    # return selected.sourceID, selected.targetID, selected.energyConsumed
    return selected

# best_jump = getMinEnergyJump([Jump(1,2,30), Jump(1,3,10), Jump(3,1,15)])
# print(str(best_jump.sourceID) + ", "+str(best_jump.targetID) + ", "+ str(best_jump.energyConsumed))

def removeJump(jumps, jump):
    jumps.remove(jump)
    print(jumps)
    return jumps


jumps = [Jump(1,2,30), Jump(1,3,10), Jump(3,1,15)]
jump= jumps[0]
# removeJump(jumps, jump)
printJumps(planets,removeJump(jumps, jump))





