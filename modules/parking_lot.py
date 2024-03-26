class Garage:    
    def __init__(self, nrOfStores, levelLength,  stairsIndexes):
        self.nrOfStores = nrOfStores
        self.levelLength = levelLength
        self.stairsIndexes = stairsIndexes

    def route(self, level, position):
        if position > self.levelLength:
            return None
        
        instructions = "" 

        steps_to_take = self.levelLength - position
        # for i in range(level, -1, -1):

        if level > 1:
            instructions += "1r, 1d, 1r, 1d, 3r"
        elif level > 0:
            instructions += "3r, 1d, 3r"
       
        elif steps_to_take == 0: 
            instructions += "You are at the exit"
        else:    
            instructions += str(steps_to_take) + "r"
        
        return instructions