import json # Used to access json-based functionality
from pathlib import Path # Used to check if the file exists and to locate its directory

# Get the directory where THIS script lives
Directory = Path(__file__).resolve().parent

# Create a path to the JSON file in that directory
file_path = Directory / "toDo.json"

if not file_path.exists():
    # Checks if the file already exists; if not, it creates a new file
    entries = {}
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(entries, file, indent=2)
else:
    # Imports data from the file if it already exists
    with open(file_path, "r", encoding="utf-8") as file:
        entries = json.load(file)

def add():
    # Prompts the user four times for input data
    task = input("Describe the task you want to add briefly " )
    details = input("Describe the task you want to add in detail " )
    due = (input("When is it due by? (MONTH/DAY/YEAR) "))
    isDone = (input("Is the task complete? (input True/False)" ))
    
    # Adds the list of strings to the dictionary which represents the data in the JSON file
    entries[task] = {
    "details": details,
    "due": due,
    "isDone": isDone == "True"
    }
    
    # Updates the JSON file with the new contents of the dictionary "entries"
    with open("toDo.json", "w") as file:
        json.dump(entries, file, indent = 2)

### Function Call
add()