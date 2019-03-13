'''
Created on 09.03.2019

@author: Nicco
'''

from testing.test_planner import test_planner


if __name__ == '__main__':
    """
    here the testing routine is started
    """
    print("Start")
    tp = test_planner()
    tp.get_available_testcases()
    tp.run()