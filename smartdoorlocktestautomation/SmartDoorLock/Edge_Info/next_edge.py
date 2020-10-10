
came_from_file_path = "Edge_Info/came_from.txt"

def change_came_from(new_came_from):
	with open(came_from_file_path, "w") as cf:
		cf.write(new_came_from)
