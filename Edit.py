from todo_database import DB
import mcp
import sys

#Structure for individual task
#brief_description(str) : [extended_description(str), time_due(str), is_completed(bool)]
#
#A list of dates that entries are due on
#entires : {
#   due_date1 : [entry1, entry2, ...],
#   due_date2 : [entry1, entry2, ...],
#   due_date3 : [entry1, entry2, ...],
#}


#entries = {}  #Creates a dictionary and converts it to a json file for the example
#exTaskDict = {'description': 'This is the example task', #'description' is the longer description while the name of the dictonary is the
#    'date_due': '0/0/0',                                 #shortened description for this example
#    'time_due': '00:00'
#    }
#entries['expTask'] = exTaskDict
#with open('json_exp.txt', 'w', encoding='utf-8') as json_file:
#    json.dump(entries, json_file)

#Loads the above json file back into a dictionary for function operation
#with open('json_exp.txt', 'r', encoding='utf-8') as f:
#    dictEx = json.load(f)


#Function needs to extract data from a json file in order to find a particular task and its corresponding details, change those details
#and then return them to the json file
@mcp.tool()
def edit():
    """Asks the user for a task then searches for that task. If the task is found it prompts the user for the data in the task then changes it. If not found, the system displays that it was not found and ends"""
    wantedEntry = input("What entry would you like to edit? Give the entry's shortened name:")
    
    entriesKeys = DB.keys() #The dictionary that is being used for storing tasks
    foundEntry = None
    for key in entriesKeys:
        if key == wantedEntry:
            foundEntry = key
            newDesc = input("Enter your new description: ")
            DB[foundEntry]['details'] = newDesc
            
            newDueDate = input("Enter your new due date: ")
            DB[foundEntry]['due date'] = newDueDate
            
            newDueTime = input("Enter your new due time: ")
            DB[foundEntry]['due time'] = newDueTime
            
            break
        
    if foundEntry is None:
        sys.stderr.write("Entry not found.")
    

#edit() #Example run