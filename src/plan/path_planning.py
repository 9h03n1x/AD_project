'''
Created on 09.03.2019

@author: Nicco
'''

from logger.logger import logger

class path_base():
    def __init__(self):
        '''
        Constructor
        '''
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
                self.heuristic[i].append(abs(distance))
        
        for line in self.heuristic:
            msg = ""
            for ele in line:
                if ele <= 9:
                    msg = msg+",  " + str(ele)
                else:
                    msg = msg+", " + str(ele)
            self.logger.write_log(msg[2:])
            
    def set_obsticals(self, static, dynamic):
        """
        set the obsticals both static an dynamic
        static and dynamic obsticals have these attributes in common
        
        array [ y1, x1, y2, x2, id] 
        """
        for  obj in static:
            if obj[0]<0 or obj[0]>len(self.grid):
                self.logger.write_log("object out of boundarys: " + str(obj))
            elif obj[1]<0 or obj[1]>len(self.grid[0]):
                self.logger.write_log("object out of boundarys: " + str(obj))
            elif obj[2]<0 or obj[2]>len(self.grid):
                self.logger.write_log("object out of boundarys: " + str(obj))
            elif obj[3]<0 or obj[3]>len(self.grid[0]):
                self.logger.write_log("object out of boundarys: " + str(obj))
            else:
                for i in range(obj[2]-obj[0]):
                    for j in range(obj[3]-obj[1]):
                        y = obj[0] + i
                        x = obj[1] + j
                        self.grid[y][x] = -1
                
        for  obj in dynamic:
            if obj[0]<0 or obj[0]>len(self.grid):
                self.logger.write_log("object out of boundarys: " + str(obj))
            elif obj[1]<0 or obj[1]>len(self.grid[0]):
                self.logger.write_log("object out of boundarys: " + str(obj))
            elif obj[2]<0 or obj[2]>len(self.grid):
                self.logger.write_log("object out of boundarys: " + str(obj))
            elif obj[3]<0 or obj[3]>len(self.grid[0]):
                self.logger.write_log("object out of boundarys: " + str(obj))
            else:
                for i in range(obj[2]-obj[0]):
                    for j in range(obj[3]-obj[1]):
                        y = obj[0] + i
                        x = obj[1] + j
                        self.grid[y][x] = -1   
    

class path_dynamic_prog(path_base):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        path_base.__init__(self)
        self.logger = logger("path_dynamic_prog")
        
    def compute_value(self,goal,cost):
        # ----------------------------------------
        # compute the values of the single grid cells
        # ----------------------------------------
        delta = [[-1, 0 ], # go up
                 [ 0, -1], # go left
                 [ 1, 0 ], # go down
                 [ 0, 1 ]] # go right

        delta_name = ['^', '<', 'v', '>']
        value = [[0 for row in range(len(self.grid[0]))] for col in range(len(self.grid))]
        closed = [[0 for row in range(len(self.grid[0]))] for col in range(len(self.grid))]
        
        x = goal[0]
        y = goal[1]
        closed[x][y]=1
        g = 0
        found = False
        resign = False
        count = 1
        option = [[g,x,y]]
        while found == False and resign == False and count < 100:
            count = count + 1
            if len(option)== 0:
                resign = True
            option.sort()
            option.reverse()
            var = option.pop()
            x = var[1]
            y = var[2]
            if x==0 and y==0:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(self.grid) and y2 >=0 and y2 < len(self.grid[0]):
                        
                        if closed[x2][y2] == 0:
                            
                            if self.grid[x2][y2]=="###":
                                value[x2][y2] = 999
                            else:
                                g = g + 1
                                value[x2][y2] = g
                                option.append([g,x2,y2])
                            closed[x2][y2] = 1
            
        # make sure your function returns a grid of values as 
        # demonstrated in the previous video.
        for line in value:
            print(line)
        return value 
        
        
class path_a_star(path_base):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        path_base.__init__(self)
        self.logger = logger("path_a_star")
        self.logger.write_log("init search A*")
    
  
    def search(self, init, goal, cost):
        # ----------------------------------------
        # modify the code below
        # init is the current position
        # ----------------------------------------
        delta_name = ['^', '<', 'v', '>']
        delta = [[-1, 0 ], # go up
                 [ 0, -1], # go left
                 [ 1, 0 ], # go down
                 [ 0, 1 ]] # go right
        closed = [[0 for col in range(len(self.grid[0]))] for row in range(len(self.grid))]
        closed[init[0]][init[1]] = 1
    
        expand = [[-1 for col in range(len(self.grid[0]))] for row in range(len(self.grid))]
        action = [[-1 for col in range(len(self.grid[0]))] for row in range(len(self.grid))]
    
        x = init[0]
        y = init[1]
        g = 0 #+ self.heuristic[x][y]
        f = g + self.heuristic[x][y]
    
        open = [[f, g, x, y]]
    
        found = False  # flag that is set when search is complete
        resign = False # flag set if we can't find expand
        count = 0
        
        while not found and not resign:
            #self.logger.write_log("iteration:" +str(count))
            if len(open) == 0:
                resign = True
                #return "Fail"
                return expand,action
            else:
                open.sort()
                open.reverse()
                next = open.pop()
                x = next[2]
                y = next[3]
                g = next[1]#+heuristic[x][y]
                f = next[0]
                expand[x][y] = count
                count += 1
                
                
                if x == goal[0] and y == goal[1]:
                    found = True
                    action[x][y]=" X "
                else:
                    for i in range(len(delta)):
                        x2 = x + delta[i][0]
                        y2 = y + delta[i][1]
                        if x2 >= 0 and x2 < len(self.grid) and y2 >=0 and y2 < len(self.grid[0]):
                            if closed[x2][y2] == 0 and self.grid[x2][y2] == 0:
                                f = g + cost[i] + self.heuristic[x2][y2]
                                open.append([f,g+1, x2, y2])
                                closed[x2][y2] = 1
                                action[x][y] = delta_name[i]
        return expand,action
        
class path_hyprid_a_star():
    '''
    '''
    def __init__(self):
        '''
        Constructor
        '''
