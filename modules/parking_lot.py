class Garage:    
    def __init__(self, nrOfStores, levelLength,  stairsIndexes):
        self.nrOfStores = nrOfStores
        self.levelLength = levelLength
        self.stairsIndexes = stairsIndexes

    def route(self, level, position):
        if position > self.levelLength:
            return None
        
        instructions =[]
        steps_to_take = position
        for i in range(level, -1, -1):
            # todo stuff, appenmd instructions 
    

        if steps_to_take == 0: 
             instructions.append("You are on the exit")
        else:    
            return instructions.append(str(position) + " left")
        
        return instructions