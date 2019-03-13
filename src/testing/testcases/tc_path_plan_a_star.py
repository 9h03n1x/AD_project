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
        self.visu = visualisation()
        self.visu.set_grid([5,5])
        #self.__set_name(self.name)
        
    def run(self):
        self.logger.write_log("start running testcase: " + self.name)
        
    
        
        