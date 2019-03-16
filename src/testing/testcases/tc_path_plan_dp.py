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
        
    def precondition_01(self):
        self.path_plan.set_grid_size(self.grid_size)
        self.visu.set_grid(self.grid_size) # hoehe x breite
        
    def teststep_01(self):
        """
        calculate the value function
        """
        goal = [10,20]
        cost = 1
        self.path_plan.compute_value(goal, cost)
