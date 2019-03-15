'''
Created on 09.03.2019

@author: Nicco
'''
from testing.testcases.tc_base import tc_base
from plan.path_planning import path_a_star
from simulator.visualisation import visualisation


class tc_path_plan_a_star(tc_base):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.name = "tc_pathplan_a_star"
        tc_base.__init__(self, self.name)
        self.path_plan = path_a_star()
        
        #self.set_name(self.name)
        self.logger.write_log("init testcase: " + self.name)
        
    def run(self):
        self.logger.write_log("start running testcase: " + self.name)
        
        
        
        
        
    def precondition_01_init_grid(self):
        """
        set the grid for the visualisation, and init the pathplanner
        """   
        grid_size = [15,25]
        self.visu = visualisation()
        self.visu.set_grid(grid_size) # hoehe x breite
        self.visu.draw_grid()
        #TODO init the a* search algo
        self.a_star = path_a_star()
        self.a_star.set_grid_size(grid_size)
        self.a_star.set_heuristic([0,0],[14,24])
        
    def precondition_02_set_obsticales(self):
        """
        set obsitcals in the grid for the visualisation
        """
        static = [[0,2,7,5], [0,5,3,15], [0,1,12,2]]
        #dynamic = [[10,10,11,12],[11,12,12,14]] # kommt später aus perception
        dynamic = []
        position = {"y":0,"x":0,"heading":"v"}
        target = {"y":14,"x":24}
        self.visu.set_ego(position)
        self.visu.set_obsticales(static, dynamic)
        self.visu.set_target(target)
        self.visu.draw_grid()
        
        