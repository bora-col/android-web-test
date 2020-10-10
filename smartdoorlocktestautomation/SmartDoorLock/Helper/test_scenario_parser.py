import json
import os
import re
import subprocess
import sys
sys.path.append('/Users/user/Desktop/smartdoorlocktestautomation/SmartDoorLock')
# print(sys.path)
from Edge_Info import next_edge

project_main_path = '/Users/user/Desktop/smartdoorlocktestautomation/SmartDoorLock'
allure_report_path = '/Users/user/Desktop/DemoReports' #smartdoorlocktestautomation/SmartDoorLock/Reports'
test_scenarios_folder = project_main_path + '/Test_Scenarios/'
function_match_filepath = project_main_path + '/Helper/function_match.json'


function_match_dict = dict()
with open(function_match_filepath, "r") as fmf:
	function_match_dict = json.load(fmf)


test_scenario_file_names_list = os.listdir(test_scenarios_folder)
test_scenario_file_names_list = [x for x in test_scenario_file_names_list if not x.startswith('.')]


for file_name in test_scenario_file_names_list:
	with open(test_scenarios_folder + file_name, "r") as f:
		lines = f.readlines()
		test_path = []
		for line in lines:
			match = re.search("({\"currentElementName\":\")(\\w+)", line.strip())
			test_path.append(match[2])

		test_path_conv = []
		for step in test_path:
			if(step[0] == 'v'):
				test_path_conv.append(function_match_dict[step])
			else:
				test_path_conv.append(step)

		for i in range(2,len(test_path_conv),2):
			e_name = test_path_conv[i-1]
			v_path = test_path_conv[i]
			next_edge.change_came_from(e_name)
			print("v_path: ", v_path)
			print("e_name: ", e_name)
			p1 = subprocess.run(['python3', '-m', 'pytest', v_path, '-s', '--alluredir', allure_report_path], capture_output=True, text=True)
			print(p1.stdout)









