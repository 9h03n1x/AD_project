'''
Created on 09.03.2019

@author: Nicco
'''

class tc_base(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.name = ""
    
    def __set_name(self,name):
        self.name = name
        
    def __name(self):
        return self.name