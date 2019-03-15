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
        self.prev_pos_ego = {}
        self.path = []
        
    def set_grid(self, size = [0,0]):
        """
        set the grid size for the planning trjectories
        """
        self.grid_size = size
        for i in range(self.grid_size[0]):
            self.grid.append([])
            for j in range(self.grid_size[1]):
                self.grid[i].append("   ")
                
    def draw_grid(self, external_grid =None):
        """
        draw the grid with the logger
        """
        if external_grid == None:
            grid = self.grid
        else:
            grid = external_grid
            
        grid_size = [len(grid),len(grid[0])]
        for i in range(grid_size[0]):
            msg = "|"
            space = "|---"
            for j in range(grid_size[1]):
                if grid[i][j] != -1:
                    ele = str(grid[i][j])
                else:
                    ele = ""
                l_ele = 3-len(ele)
                ele = l_ele*" " + ele
                msg = msg + ele +"|"
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
        
    def set_ego(self, position, keep_history = True):
        """
        set the ego position of the current vehicle
        """
        if keep_history == False:
            self.grid[self.prev_pos_ego["y"]][self.prev_pos_ego["x"]] = "   "
            
        cell =self.grid[position["y"]][position["x"]]
        if cell != "dyn" or cell != "###":
            if keep_history == False:
                self.grid[self.prev_pos_ego["y"]][self.prev_pos_ego["x"]] = "   "
            self.grid[position["y"]][position["x"]] = " "+position["heading"]+" "
            self.prev_pos_ego = position
            self.path.append(position)
                    
    def set_target(self, position):
        """
        set the target position in the grid for the target location
        """
        cell =self.grid[position["y"]][position["x"]]
        if cell != "dyn" or cell != "###":
            self.grid[position["y"]][position["x"]] = " X "
        
                
        
        
        
        