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
        self.direction = ""
    def set_position(self,x,y,theta):
        self.position = {"x": x, "y": y, "theta": theta}
        

    def update_position(self, movement, step=1):
        """
        update the postion of the ego according to a movement in a direction
        movement gives the new position, from this and the old postion te direction will be calculated
        step gives how many cells are covered in this direction
        """
        delta_x = self.position["x"] - movement[0]
        delta_y = self.position["y"] - movement[1]
        
        if delta_x == -1 and delta_y == 0:
            direction = "N"
        elif delta_x == 0 and delta_y == -1:
            direction = "E"
        elif delta_x == 1 and delta_y == 0:
            direction = "S"
        elif delta_x == 0 and delta_y == 1:
            direction = "W"
        else:
            direction=self.position["theta"]
        
        self.logger.write_log("delta_x: " +str(delta_x) + "\tdelta_y: " + str(delta_y) + "\tdirection: " + direction)
        
        
        for i in range(0,step):
            self.position["x"] += self.move[direction][1] 
            self.position["y"] += self.move[direction][0]
            self.position["theta"] = direction
        
    def get_move_options(self):
        """
        return the options according to the current position, assuming that the ego is not able to reverse
        """
        move_opt = []
        name_opt = []
        directions = self.move_name[self.position["theta"]]
        for direction in directions:
            move_opt.append(self.move[direction])
        
        if self.position["theta"] == "N":
            name_opt = ["L", "^", "R"]
        elif self.position["theta"] == "S":
            name_opt = ["L", "v", "R"]
        elif self.position["theta"] == "E":
            name_opt = ["R", ">", "L"]
        elif self.position["theta"] == "W":
            name_opt = ["R", "<","L"]
        else:
            pass
        #TODO: mapping auf left,straigt,right aus sicht des EGO
            
        return move_opt, name_opt
        
    def get_direction(self, direction):
        """
        returns the symbol of current movement
        """
        
        if self.direction == direction:
            val = "s_"
            options = self.move_name[direction]
        elif self.direction == "":
            val = "n_"
            options = "NWSE"
        else:
            options = self.move_name[direction]
            
            if self.direction == options[0]:
                val = "R_"
            elif self.direction == options[2]:
                val = "L_"
            else:
                val = "-_"
                self.logger.write_log("direction: " + str(direction) + "\t options: " + str(options))
        self.direction = direction    
        val = val + direction
        delta = []
        delta_names = []
        for ele in options:
            delta_names.append(ele)
            delta.append(self.move[ele])
        return val
                
 