'''
Created on 10.03.2019

@author: Nicco
'''

class logger():
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        self.parent = parent
        
    def write_log(self, msg, level = "DEBUG"):
        """
        log the message to the console
        """
        log = level + "\t" + self.parent +"\t" +msg
        print(log)
        
    
        