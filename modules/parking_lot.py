class Garage:    
    def __init__(self, levelLength, stairsIndexes):
        self.levelLength = levelLength
        self.stairsIndexes = stairsIndexes

    def route(self, level, position):
        if position > self.levelLength:
            return None
        
        return [str(position) + " left"]