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
        self.position["x"] = x
        self.position["y"] = y
        self.position["theta"] = theta