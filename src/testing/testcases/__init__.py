from . import tc_path_plan_a_star
from . import tc_path_plan_dp
from . import tc_path_plan_a_star_road

# All of this has to be automated later

tc_list = []
tc_available_tcs = []

tc_available_tcs.append("tc_path_plan_a_star")
tc_available_tcs.append("tc_path_plan_a_star_road")
tc_available_tcs.append("tp_path_plan_dp")

tc_list.append(tc_path_plan_a_star.tc_path_plan_a_star)
tc_list.append(tc_path_plan_dp.tp_path_plan_dp)
tc_list.append(tc_path_plan_a_star_road.tc_path_plan_a_star_road)

def get_available_tc():
    tc_dict = {}
    for name in tc_available_tcs:
        tc_dict[name] = tc_list[tc_available_tcs.index(name)]
    return tc_dict

def get_tc_names():
    return tc_available_tcs