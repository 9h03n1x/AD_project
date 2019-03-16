'''
Created on 09.03.2019

@author: Nicco
'''
from testing.testcases.tc_base import tc_base
from plan.path_planning import path_dynamic_prog
from simulator.visualisation import visualisation


class tp_path_plan_dp(tc_base):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.name = "tp_path_plan_dp"
        tc_base.__init__(self,self.name)
        #self.__set_name(self.name)
        self.path_plan = path_dynamic_prog()
        self.visu = visualisation()
        self.grid_size=[15,25]
        
    def precondition_01_init_pathplan(self):
        """
        init the pathplanning algo and the visualisation
        """
        self.path_plan.set_grid_size(self.grid_size)
        self.visu.set_grid(self.grid_size) # hoehe x breite
    
    def precondition_02_set_obsticals(self):
        """
        set the defined obsticals in both grid, pathplanner and visu
        """
        self.static = [[0,2,7,5], 
                       [0,5,3,15], 
                       [0,1,12,2],
                       [13,10,15,20],
                       [8,14,13,17]]
        self.path_plan.set_obsticals(self.static,[]) 
        self.visu.set_obsticales(self.static,[])
        self.visu.draw_grid(self.path_plan.get_grid())
        
    def teststep_01(self):
        """
        calculate the value function
        """
        goal = [10,20]
        cost = [1,1,1,1]
        value_grid, policy_grid = self.path_plan.compute_value(goal, cost)
        self.logger.write_log("value_grid: ")
        self.visu.draw_grid(value_grid)
        
        self.logger.write_log("policy_grid: ")
        self.visu.draw_grid(policy_grid)