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
        self.visu.set_grid([15,25]) # hoehe x breite
        #self.set_name(self.name)
        
    def run(self):
        self.logger.write_log("start running testcase: " + self.name)
        #self.visu.draw_grid()
        
        
        static = [[2,2,7,5], [2,5,3,15]]
        dynamic = [[10,10,12,14]] # kommt später aus perception
        position = {"y":0,"x":0,"heading":"v"}
        
        self.visu.set_ego(position)
        self.visu.set_obsticales(static, dynamic)
        self.visu.draw_grid()
        
        