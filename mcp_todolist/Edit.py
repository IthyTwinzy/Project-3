from todo_database import DB
from typing import Annotated
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
def edit_task(requestedEntry: Annotated[str, "The name of the task that the user wants to edit."],
         newDescription: Annotated[str, "A description of the task."] | None=None,
         newDate: Annotated[str, "The date the task is due on, format as numbers in the form of MONTH/DAY/YEAR"] | None=None,
         newTime: Annotated[str, "The time the task is due at on the given day, format as a 24 hour digital clock in the form of 00:00"] | None=None)
    """Changes a specific task in the list of tasks based on the parameters provided"""
    
    if requestedEntry in DB.data:
        
        if newDescription != None:
            DB.data[requestedEntry]['details'] = newDescription
        if newDate != None:
            DB.data[requestedEntry]['due date'] = newDate
        if newTime != None:
            DB.data[requestedEntry]['due time'] = newTime
            
    

#edit() #Example run