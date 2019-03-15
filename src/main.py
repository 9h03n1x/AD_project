'''
Created on 09.03.2019

@author: Nicco
'''

from testing.test_planner import test_planner
from logger.logger import logger



if __name__ == '__main__':
    """
    here the testing routine is started
    """

    tp = test_planner()
    log = logger("main")
    tp.get_available_testcases()
    res = []
    for i in range(0,1):
        results = tp.run()
    
    avg_dur = 0
    count = 0
    log.write_log("--------------------------------------------------------")
    for res in results:
        if res["name"] == "tc_path_plan_a_star":
            avg_dur = avg_dur + res["duration"]
            count+=1
            log.write_log(res["name"] + ":\t result " + str(res["result"]) + "\t duration:" + str(res["duration"])[:6]  )
    log.write_log("--------------------------------------------------------")
    log.write_log("average testcase duration: " +str(avg_dur/count)[:6])
   
    
