"""
created 16.03.2019
@author: Nicco
"""
from .ego_base import ego_base

class simple_ego(ego_base):
    
    def __init__(self):
        ego_base.__init__(self)
        
        self.position = {"x": 0, "y": 0, "theta": "N"}
        self.move_name = {"N":"WNE", "E":"NES", "S":"ESW", "W":"SWN"}
        self.move = {"N":[-1, 0 ],
                     "E":[ 0, -1],
                     "S":[ 1, 0 ],
                     "W":[ 0, 1 ]}

    def update_position(self, movement):
        self.position["x"] += self.move[movement][1] 
        self.position["y"] += self.move[movement][0]
        self.position["theta": movement]
        
    
        