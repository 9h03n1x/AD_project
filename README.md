AD_project

This Project is a test to put up a AD-Chain starting from Perception, over the PLAN and to the act part,
This is based on the Udacity Nanodegree for self driving car engineer

This Project will contain the possiblity to set up testcases in the testcase folder and execute those using the testplanner

The Project consist of the Following Modules:

  - act: modelling the actors of the vehicle
  - perception: modelling the perception algo's 
  - plan: modelling the search algo's and behavior planner
    - path_planning:
      - A* Planner (Implemented):
        also has now a dynamic cost function 
      - Dynamic Programming Planner (under work, compute value is done)
      - Hypbrid A* Planner (not yet implemented)
  - ego: describing a simple motion modell
    - ego_base: providing the basic features for ego modells
    - simple_ego: very simple motion modell for the first algo's
  - testing: containing the testplanner and the testcases
  - logger: a logger utility for better debugging purposes
  
So far only one testcase is implemented, the testcase for the A* Algo

To run the testcase, just clone the repo and run the main.py

How To add a Testcase:

1. Create a new Testcase file in the testcase folder
2. the Class in the testcase file has to have a "__init__" method, 
    the different teststeps and preconditions as well as the post conditions are methods as well, for example to add a precondition   step,
      define a method called
        def preconditon_01_first(self):
  
   for the second step in the preconditions just ad another method, called precondition_02(self), please do not pass parameters via the   teststeps
    to add a teststep:
      def teststep_01(self):
  
3. Now the testcase has to be registered in the init.py file of the testcase module
  - import the testcase
    from . import tc_my_testcase
  - add the testcase to the testcase name list
    tc_available_tcs.append("name of my new testcase")
  - add the testcase class to the execution list
    tc_list.append(tc_my_testcase.tc_my_testcase)

