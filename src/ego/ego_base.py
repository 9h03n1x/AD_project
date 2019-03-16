'''
created 16.03.2019

@author: Nicco
'''
from logger.logger import logger

class ego_base():
    
    def __init__(self):
        self.logger = logger("ego")
        self.position = {}
        
    def get_position(self):
        return self.position
    
    def set_position(self,x,y,theta):
        """
        set the initial postion of the ego
        x,y = int within the grid
        theta: str "N","E","S","W"
        """
        self.position["x"] = x
        self.position["y"] = y
        self.position["theta"] = theta
    
    