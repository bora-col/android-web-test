import json
from SmartDoorLock.Helper.door_status import DoorStatus
print("__file__", __file__)
# from SmartDoorLock import __file__
import os


class ParseData:
    # Define the variables will be used
    office_id = ""
    status = ""
    door_id = ""

    # Create a DoorStatus object.
    # Call connect_socketio function
    # Read the data.json file and handle it.
    @staticmethod
    def parse_data(json_file_name):
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_file_path = root_dir + "/Json/" + json_file_name
        # print()
        # print("parse_data.py -> parse_data() -> json_file_path = " + json_file_path)
        # print()
        # DoorStatus.json_file_path = json_file_path
        door_status = DoorStatus(json_file_path)

        connect = door_status.connect_socketio
        connect()
        with open(json_file_path) as json_file:
            data = json.load(json_file)
            office_id = data['office_id']
            status = data['status']
            door_id = data['door_id']
            return office_id, status, door_id
