import sys
import pytest
sys.path.append('/Users/user/Desktop/smartdoorlocktestautomation')
from SmartDoorLock.Helper.parse_data import ParseData

office_id, status, door_id = ParseData.parse_data("data_mobile_embedded.json")
came_from_file_path = "Edge_Info/came_from.txt"




class TestFunctional:

	my_came_from = None;

	@pytest.fixture(scope="function")
	def edge_info(self):
		with open(came_from_file_path, "r") as cf:
			lines = cf.readlines()
			for line in lines:
				self.my_came_from = line.strip()

		print("init->my_came_from: ", self.my_came_from)


	def e_print_hello(self):
		print("Hello")


	# Office id should be 1
	def test_office_id(self,edge_info):
	    print("\nOffice ID is: " + str(office_id))
	    assert office_id == 1


	# Status should be between -1 and 4
	# -1 means status is unknown
	#  0 means status is Open/Unlocked
	#  1 means status is Closed/Unlocked
	#  2 means status is Close/Lock
	#  3 means status is Busy
	#  4 means status is Waiting
	def test_status(self,edge_info):
	    print("\nStatus is: " + str(status))
	    assert status in [-1, 0, 1, 2, 3, 4]


	# Door id should be 2
	def test_door_id(self,edge_info):
		# print("test->my_came_from: ", self.my_came_from)
		edge_to_call = getattr(globals()['TestFunctional'](), self.my_came_from)
		edge_to_call()
		print("\nDoor ID is: " + str(door_id))
		assert door_id == 2
