'''
Created on 09.03.2019

@author: Nicco
'''
from logger.logger import logger


class tc_base(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.logger = logger(name)
    
    def set_name(self,name):
        self.name = name
        
    def __name(self):
        return self.name