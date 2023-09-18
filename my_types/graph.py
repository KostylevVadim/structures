class Graph:
    def __init__(self, matrix: dict):
        self.__matrix = matrix
    
    def is_near(self,data, x):
        z = self.__matrix.keys()
        if data in z:
            if x in self.__matrix[data]:
                return True
            else:
                return False
        else:
            return False
    
    
