'''
Created on 09.03.2019

@author: Nicco
'''
from testing import testcases

class test_planner(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.list_tc = []
    
    def get_available_testcases():
        """
        append all testcases to the tc_list
        """ 
        tc = testcases.tc_path_plan_a_star.tc_path_plan_a_star()
    
    def run(self):
        for tc in self.list_tc:
            print("-------------------------------------------------")
            print("running testcase: " + tc.__name())
            tc.run()