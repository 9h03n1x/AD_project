'''
Created on 09.03.2019

@author: Nicco
'''

from logger.logger import logger

class visualisation(object):
    '''
    visualize the the data coming from different modules, such as pathplannig etc.
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.logger = logger()
        self.grid = []
        self.grid_size = []
        self.static_obj = []
        self.dynamic_obj = []
        
        
    def set_grid(self, size = [0,0]):
        """
        set the grid size for the planning trjectories
        """
        self.grid_size = size
        for i in range(self.size[0]):
            self.grid.append([])
            for j in range(self.size[1]):
                self.grid[i].append("   ")
                
    def draw_grid(self):
        """
        draw the grid with the logger
        """
        for i in range(self.size[0]):
            msg = ""
            for j in range(self.size[1]):
                msg = msg + self.grid[i][j]
            self.logger._write_logs(msg, "_SIM_")
                
        
    def set_obsticales(self, static = [], dynamic = []):
        """
        set the obsticals both static an dynamic
        """
        
        