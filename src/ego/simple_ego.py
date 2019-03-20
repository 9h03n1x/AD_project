"""
created 16.03.2019
@author: Nicco
"""
from .ego_base import ego_base

class simple_ego(ego_base):
    
    def __init__(self):
        ego_base.__init__(self)
        self.length = 1
        self.position = {"x": 0, "y": 0, "theta": "N"}
        self.move_name = {"N":"WNE", "E":"NES", "S":"ESW", "W":"SWN"}
        self.move = {"N":[-1, 0 ],
                     "E":[ 0, -1],
                     "S":[ 1, 0 ],
                     "W":[ 0, 1 ]}

    def update_position(self, movement, step=1):
        """
        update the postion of the ego according to a movement in a direction
        movement givs the direction using a string 
        step gives how many cells are covered in this direction
        """
        for i in range(0,step):
            self.position["x"] += self.move[movement][1] 
            self.position["y"] += self.move[movement][0]
            self.position["theta": movement]
        
    def get_move_options(self):
        """
        return the options according to the current position, assuming that the ego is not able to reverse
        """
        move_opt = {}
        directions = self.move_name[self.position["theta"]]
        for direction in directions:
            move_opt[direction]=self.move[direction]
            
        return move_opt
        