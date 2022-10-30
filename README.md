Let's go with the AirBnB task.(it is goint to be a hard one so hold on to your ones and zeros)

Description of the project:

This project will span over the next couple of months. It will be compiled on several different occasions to improve the design and usability of the project.
With this project we are set out to create a clone of the website AirBnB.
It will consist out of several different tasks aswell as components to create a real feel clone of the website. For the first part of our ABnB project we need a command line interpreter(CLI).

We are going to use the CLI for several commands and purposes but for now, it is used to modify database engines aswell as the file.json (the file storage engine).
We will be able to :
#-Create a new object (ex: a new User or a new Place)
#-Retrieve an object from a file, a database ect.
#-Do operations on objects (count, compute stats, ect)
#-Update attributes of an object
#-Destroy an object

(Oh what fun this is going to be....some hard fun)

The CLI would be used as such:

My command interpreter implements:

	quit and EOF to exit the program
	help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
	a custom prompt: (hbnb)
	an empty line + ENTER shouldn’t execute anything
	create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
	show: Prints the string representation of an instance based on the class name and id
	destroy: Deletes an instance based on the class name and id (save the change into the JSON file)
	all: Prints all string representation of all instances based or not on the class name.
	update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)

We can assume the following rules:

You can assume arguments are always in the right order
Each arguments are separated by a space
A string argument with a space must be between double quote
The error management starts from the first argument to the last one

=============================================================================================================================================
To start the CLI we use the command ./console.py
This is a executable file used to run the console (CLI) program.
Example:

$./console.py
(hbnb)
(hbnb)

Using the CLI:

There are several usages of the console (CLI), but the most common one touse would be the "help" command.
Typing this command will list the available commands to assist you to use the console.
It would look something like this:

(hbnb)help

Documented commands (type help \<topic\>):
==========================================================
EOF  all  clear  create  destroy  help  quit  show  update

(hbnb)
(hbnb)quit
$

To use functions one simply put the function name and an argument which is tied to the function.

Some examples are:

$./console.py


