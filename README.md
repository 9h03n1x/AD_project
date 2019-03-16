AD_project

This Project is a test to put up a AD-Chain starting from Perception, over the PLAN and to the act part,
This is based on the Udacity Nanodegree for self driving car engineer

This Project will contain the possiblity to set up testcases in the testcase folder and execute those using the testplanner

The Project consist of the Following Modules:

  - act: modelling the actors of the vehicle
  - perception: modelling the perception algo's 
  - plan: modelling the search algo's and behavior planner
    - path_planning:
      - A* Planner (Implemented)
      - Dynamic Programming Planner (not yet implemented)
      - Hypbrid A* Planner (not yet implemented)
  - ego: describing a simple motion modell
  - testing: containing the testplanner and the testcases
  - logger: a logger utility for better debugging purposes
  
So far only one testcase is implemented, the testcase for the A* Algo

To run the testcase, just clone the repo and run the main.py

