'''
Created on 09.03.2019

@author: Nicco
'''

from logger.logger import logger

class visualisation(object):
    '''
    visualize the the data coming from different modules, such as pathplannig etc.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.logger = logger("simulator")
        self.grid = []
        self.grid_size = []
        self.static_obj = []
        self.dynamic_obj = []
        
        
    def set_grid(self, size = [0,0]):
        """
        set the grid size for the planning trjectories
        """
        self.grid_size = size
        for i in range(self.grid_size[0]):
            self.grid.append([])
            for j in range(self.grid_size[1]):
                self.grid[i].append("   ")
                
    def draw_grid(self):
        """
        draw the grid with the logger
        """
        for i in range(self.grid_size[0]):
            msg = "|"
            space = "|---"
            for j in range(self.grid_size[1]):
                msg = msg + self.grid[i][j]+"|"
                space = space + "|---"
            self.logger.write_log(space[:-3], "_SIM_")
            self.logger.write_log(msg, "_SIM_")
        self.logger.write_log(space[:-3], "_SIM_")
        self.logger.write_log(len(msg)*"#" + "\n") 
                
        
    def set_obsticales(self, static = [], dynamic = []):
        """
        set the obsticals both static an dynamic
        static and dynamic obsticals have these attributes in common
        
        array [ y1, x1, y2, x2, id] 
        """
        for  obj in static:
            if obj[0]<0 or obj[0]>len(self.grid):
                self.logger.write_log("object out of boundarys: " + str(obj))
            elif obj[1]<0 or obj[1]>len(self.grid[0]):
                self.logger.write_log("object out of boundarys: " + str(obj))
            elif obj[2]<0 or obj[2]>len(self.grid):
                self.logger.write_log("object out of boundarys: " + str(obj))
            elif obj[3]<0 or obj[3]>len(self.grid[0]):
                self.logger.write_log("object out of boundarys: " + str(obj))
            else:
                for i in range(obj[2]-obj[0]):
                    for j in range(obj[3]-obj[1]):
                        y = obj[0] + i
                        x = obj[1] + j
                        self.grid[y][x] = "###"
                
        for  obj in dynamic:
            if obj[0]<0 or obj[0]>len(self.grid):
                self.logger.write_log("object out of boundarys: " + str(obj))
            elif obj[1]<0 or obj[1]>len(self.grid[0]):
                self.logger.write_log("object out of boundarys: " + str(obj))
            elif obj[2]<0 or obj[2]>len(self.grid):
                self.logger.write_log("object out of boundarys: " + str(obj))
            elif obj[3]<0 or obj[3]>len(self.grid[0]):
                self.logger.write_log("object out of boundarys: " + str(obj))
            else:
                for i in range(obj[2]-obj[0]):
                    for j in range(obj[3]-obj[1]):
                        y = obj[0] + i
                        x = obj[1] + j
                        self.grid[y][x] = "dyn"
        
    def set_ego(self, position):
        """
        """
        cell =self.grid[position["y"]][position["x"]]
        if cell != "dyn" or cell != "###":
            self.grid[position["y"]][position["x"]] = " "+position["heading"]+" "
                    

                
        
        
        
        