import json
import socketio
import SmartDoorLock.Configuration.base_config as base_config


json_file_path = ""

# Get door status via socket.io
class DoorStatus:
    # A socket.io client is created
    sio = socketio.Client()
    # data variable is defined in the class level.
    data = None
    # json_file_path = None

    def __init__(self, in_json_file_path):
        global json_file_path, driver
        json_file_path = in_json_file_path
        self.json_file_path = in_json_file_path
        print("door_status.py -> __init__() -> self.json_file_path = ", self.json_file_path)


    @staticmethod
    def door_status_handler(data=None):
        print("data is received: ", data)
        with open(json_file_path, 'r+') as data_file:
            data_file.truncate(0)
            json.dump(data, data_file)
        if data['status'] in [0,1,2]:
            DoorStatus.sio.disconnect()




    # write data in a json file
    # @classmethod
    # def door_status_handler(cls,data=None):
    #     print()
    #     print("data is received: ", data)
    #     print("json_file_path = ", cls.json_file_path)
    #     #print("type(self)",end="")
    #     #print(type(self))
    #     #print("self", self)
    #     print()

    #     with open(cls.json_file_path, 'w') as data_file:
    #         json.dump(data, data_file)

    #     # json.dump(data,self)
    #     #data = self.copy()
    #     if data['status'] == 1:
    #         DoorStatus.sio.disconnect()




    # def door_status_handler(self,data=None):
    #     print()
    #     print("data is received: ", data)
    #     print("json_file_path = ", DoorStatus.json_file_path)
    #     #print("type(self)",end="")
    #     #print(type(self))
    #     print("self", self)
    #     print()
    #     # with open(json_file_path, 'w') as data_file:
    #     #     json.dump(data, data_file)
    #     # json.dump(data,self)
    #     data = self.copy()
    #     # if data['status'] == 0:
    #     DoorStatus.sio.disconnect()




    # Receive data
    @staticmethod
    def door_connection_handler(data=None):
        # print()
        # print("door_status.py -> door_connection_handler() -> data = ", data)
        # print()
        return data

    @sio.event
    def connect(self=None):
        # print()
        # print("door_status.py -> connect() -> self = ", self)
        # print()
        DoorStatus.sio.on("connection", DoorStatus.door_connection_handler)
        DoorStatus.sio.emit("subscribe", {"office_id": 1})
        DoorStatus.sio.on("door_status_notify", DoorStatus.door_status_handler)
        DoorStatus.sio.emit("get_door_status", {"door_id": 234523, "office_id": 1})

    # Disconnect from the server
    @sio.event()
    def disconnect():
        DoorStatus.sio.disconnect()
        DoorStatus.sio.eio.disconnect(True)

    # Connect to the server
    @staticmethod
    def connect_socketio():
        url = base_config.Configuration.get_base_url()
        # print()
        # print("door_status.py -> connect_socketio() -> url = " + url)
        # print()
        password = base_config.Configuration.get_mobile_device_password()
        # print()
        # print("door_status.py -> connect_socketio() -> password = " + password)
        # print()
        path = base_config.Configuration.get_socket_path()
        # print()
        # print("door_status.py -> connect_socketio() -> path = " + path)
        # print()
        DoorStatus.sio.connect(url + password, socketio_path=path)
        DoorStatus.sio.wait()
        # print()
        # print("door_status.py -> connect_socketio() -> HERE1")
        # print()

    # Disconnect from the socket.io
    @staticmethod
    def disconnect_socketio():
        DoorStatus.sio.disconnect()
        DoorStatus.sio.eio.disconnect(True)
