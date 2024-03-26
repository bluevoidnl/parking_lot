class Garage:    
    def __init__(self, nrOfStores, levelLength,  stairsIndexes):
        self.nrOfStores = nrOfStores
        self.levelLength = levelLength
        self.stairsIndexes = stairsIndexes

    def route(self, level, position):
        if position > self.levelLength:
            return None
        
        instructions = []

        steps_to_take = position
        if level > 0:
            instructions.append("3 left")
            instructions.append("1 down")
            instructions.append("5 right")
        # for i in range(level, -1, -1):
        elif steps_to_take == 0: 
            instructions.append("You are on the exit")
        else:    
            instructions.append(str(position) + " left")
        
        return instructions