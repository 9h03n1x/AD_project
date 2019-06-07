'''
Created on 09.03.2019

@author: Nicco
'''
from testing.testcases.tc_base import tc_base
from plan.path_planning import path_dynamic_prog
from simulator.visualisation import visualisation


class tc_path_plan_dp_road(tc_base):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.name = "tc_path_plan_dp_road"
        tc_base.__init__(self, self.name)
        self.path_plan = path_dynamic_prog()
        
        #self.set_name(self.name)
        self.logger.write_log("init testcase: " + self.name)
        
        # define the testcase variable:
        self.position = {"y":14,"x":14,"heading":"^"}
        self.target = {"y":6,"x":0}
        self.static = [[0,0,6,14], 
                       [7,0,15,14], 
                       [1,15,6,24],
                       [7,15,13,25],
                       [13,15,15,25]]

    def precondition_01_init_grid(self):
        """
        set the grid for the visualisation, and init the pathplanner
        """   
        grid_size = [15,25]
        self.visu = visualisation()
        self.visu.set_grid(grid_size) # hoehe x breite
        #TODO init the a* search algo
        self.path_plan = path_dynamic_prog()
        self.path_plan.set_grid_size(grid_size)
        init = [self.position["y"],self.position["x"]]
        goal = [self.target["y"],self.target["x"]]
        
        
    def precondition_02_set_obsticales(self):
        """
        set obsitcals in the grid for the visualisation
        """
        static = self.static
        #dynamic = [[10,10,11,12],[11,12,12,14]] # kommt später aus perception
        dynamic = []
        position = self.position
        target = self.target
        self.visu.set_ego(position)
        self.visu.set_obsticales(static, dynamic)
        self.visu.set_target(target)
        self.visu.draw_grid()
        self.path_plan.set_obsticals(static, [])
        
    def teststep_01(self):
        position = self.position
        target = self.target
        static = self.static
        cost = [1,1,1,1]
        self.path_plan.set_obsticals(static, [])
        goal = [self.target["y"],self.target["x"]]
        value_grid, policy_grid = self.path_plan.compute_value(goal, cost)
        self.logger.write_log("value_grid")
        self.visu.draw_grid(value_grid)
        self.logger.write_log("policy_grid")
        self.visu.draw_grid(policy_grid)
        