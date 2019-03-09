'''
Created on 09.03.2019

@author: Nicco
'''

class test_planner(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.list_tc = []
        
    
    def run(self):
        for tc in self.list_tc:
            print("-------------------------------------------------")
            print("running testcase: " + tc.__name())
            tc.run()