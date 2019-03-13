'''
Created on 09.03.2019

@author: Nicco
'''
from testing.testcases import tc_path_plan_a_star as testcase
from logger.logger import logger

class test_planner(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.list_tc = []
        self.logger = logger("test_planner")
    
    def get_available_testcases(self):
        """
        append all testcases to the tc_list
        """ 
        tc = testcase.tc_path_plan_a_star()
        self.list_tc.append(tc)
    
    def run(self):
        for tc in self.list_tc:
            self.logger.write_log("-------------------------------------------------")
            self.logger.write_log("running testcase: " + tc.name)
            tc.run()