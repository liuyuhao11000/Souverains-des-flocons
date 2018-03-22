from hexagrid import *
from model import *
import multiprocessing as mp

class Controller:
    def __init__(self, alpha, beta, gamma, mapRadius):
        self.model = Model(alpha, beta, gamma, mapRadius)
        self.nbCellsWidth = self.model.hexaMap.nbCellsWidth
        self.ResetGrid()
        
    def ResetGrid(self):
        self.model.InitGrid()
    
    def NextStep(self):
        self.model.UpdateGrid()
