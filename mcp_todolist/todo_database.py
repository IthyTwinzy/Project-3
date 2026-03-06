import atexit
import json 
import os

# Stores data for the todo list database (this should only be initialized once)
class TodoDatabase:
    """Stores and updates todolist data"""
    
    # Populates the database using the data in the json file
    def __init__(self) -> None:
        """Populates the database from a json file"""

        self.data: dict = {}       # This is what will be writen back to the json and stores a flattened todo list

        # Populates the "data" dictionary with data from the file
        if os.path.exists("output/tasks.json") and os.path.getsize("output/tasks.json") != 0:
            with open("output/tasks.json", 'r') as task_file:
                self.data = json.load(task_file)

        # Makes the database close automatically on exit
        atexit.register(self.close)

    # Writes data in the database back to the json file
    def close(self):
        """Writes todo list to the json file"""
    
        # Creates the output directory
        if not os.path.exists("output"):
            os.mkdir("output")

        with open("output/temp.json", 'w') as task_file:
            json.dump(self.data, task_file, indent=2)
        os.replace("output/temp.json", "output/tasks.json")

# Varriable that stores the darabase that will be used by this program
DB = TodoDatabase()