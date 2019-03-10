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
        if len(self.parent)> 13:
            spacer = "\t"
        else:
            spacer = "\t\t"
        
        log = level + "\t" + self.parent +spacer +msg
        print(log)
        
    
        