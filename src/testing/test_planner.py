'''
Created on 09.03.2019

@author: Nicco
'''
from . import testcases
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
        self.list_tc = {}
        self.list_tc_init={}
        self.logger = logger("test_planner")
    
    def get_available_testcases(self):
        """
        append all testcases to the tc_list
        """ 
        self.list_tc = testcases.get_available_tc()
        for key in self.list_tc.keys():
            self.list_tc_init[key] = self.list_tc[key]()
            
        
    
    def run(self):
        for tc_key in self.list_tc.keys():
            self.logger.write_log("-------------------------------------------------")
            self.logger.write_log("running testcase: " + tc_key)
            
            tc_obj = self.list_tc_init[tc_key]
            tc_class = self.list_tc[tc_key]
            preCon_keys = []
            testStep_keys = []
            postCon_keys = []
            for m_key in tc_class.__dict__.keys():
                if m_key.find("precondition") != -1:
                    preCon_keys.append(m_key)
                elif m_key.find("teststep") != -1:
                    testStep_keys.append(m_key)
                elif m_key.find("postcondition") != -1:
                    testStep_keys.append(m_key)   
                    
            # sort the teststeps
            preCon_keys.sort()
            testStep_keys.sort()
            postCon_keys.sort()
            self.logger.write_log("-------------------------------------------------")
            self.logger.write_log("running precondition: " + tc_key)
            for preCon in preCon_keys:
                self.logger.write_log("running precondition: " + preCon + "\n")
                tc_class.__dict__[preCon](tc_obj)
            self.logger.write_log("-------------------------------------------------")   
            self.logger.write_log("running teststeps: " + tc_key)
            for teststep in testStep_keys:
                self.logger.write_log("running teststep: " + teststep + "\n")
                tc_class.__dict__[teststep](tc_obj)
            self.logger.write_log("-------------------------------------------------")   
            self.logger.write_log("running postcondition: " + tc_key)
            for postCon in postCon_keys:
                self.logger.write_log("running postcondition: " + postCon + "\n")
                tc_class.__dict__[postCon](tc_obj)
            
            self.logger.write_log("-------------------------------------------------")
            self.logger.write_log("finished testcase: " + tc_key)  
            