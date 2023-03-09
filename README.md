### AirBnB CLONE PROJECT - THE CONSOLE

This directory contains the first AirBnB clone project. The core part of this project is 'The Console', with its commands to create, update, destroy, and show objects of an AirBnB

### The Console

i. create your data model
ii. manage (create, update, destroy, etc) objects via a console / command interpreter
iii. store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine


### Contents Of Directories

i. Models Folder: Classes of the project. BaseModel is the parent Class while other classes (amenity, city, place, review, state, user(children classes)) inherit from BaseModel.
ii. Tests Folder : Unittests for the project
iii. AUTHORS: Information about the authors
iv. console.py: Eceutable file for the console
v. file.json: JSON file with all information of instances


### Installation
Clone the repository; git clone https://github.com/tsionassefa/AirBnB_clone
Open the /AirBnB_clone directory and execute console.py

You need to have python installed on your machine.


### Example

## Execution

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$


