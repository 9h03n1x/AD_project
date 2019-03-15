'''
Created on 09.03.2019

@author: Nicco
'''

from logger.logger import logger

class path_dynamic_prog(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        
class path_a_star(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.logger = logger("path_a_star")
        self.logger.write_log("init search A*")
        self.grid = []
        self.grid_size=[]
        self.heuristic = []
        self.open = []
        
    def set_grid_size(self, size):
        self.grid_size = size
        for i in range(self.grid_size[0]):
            self.grid.append([])
            for j in range(self.grid_size[1]):
                self.grid[i].append(0)
    
    def set_heuristic(self,init,target):
        """
        set up the heuristic for the search pattern
        """
        self.logger.write_log("init the heuristic function")
        for i in range(self.grid_size[0]):
            self.heuristic.append([])
            for j in range(self.grid_size[1]):
                distance = 0
                distance = (target[0]-init[0])+(target[1]-init[1])
                distance = distance - i - j
                self.heuristic[i].append(distance)
            self.logger.write_log(self.heuristic[i])           
        
    def search(self, init):
        # ----------------------------------------
        # modify the code below
        # init is the current position
        # ----------------------------------------
        closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        closed[init[0]][init[1]] = 1
    
        expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
        action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    
        x = init[0]
        y = init[1]
        g = 0 + heuristic[x][y]
    
        open = [[g, x, y]]
    
        found = False  # flag that is set when search is complete
        resign = False # flag set if we can't find expand
        count = 0
        
        while not found and not resign:
            if len(open) == 0:
                resign = True
                return "Fail"
            else:
                open.sort()
                open.reverse()
                next = open.pop()
                x = next[1]
                y = next[2]
                g = next[0]#+heuristic[x][y]
                expand[x][y] = count
                count += 1
                
                
                if x == goal[0] and y == goal[1]:
                    found = True
                else:
                    for i in range(len(delta)):
                        x2 = x + delta[i][0]
                        y2 = y + delta[i][1]
                        if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                            if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                                g2 = g + cost + heuristic[x2][y2]
                                open.append([g2, x2, y2])
                                closed[x2][y2] = 1
                                action[x][y] = delta_name[i]
        for ele in action:
            print(ele)
        return expand
        
class path_hyprid_a_star():
    '''
    '''
    def __init__(self):
        '''
        Constructor
        '''