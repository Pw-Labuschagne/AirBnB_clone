#!/usr/bin/python3
"""A command line intepreter tool used for AirBnB project"""
import cmd
import readline
import re
from os import system
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity


def parser(argu):
    """Main parsing fucntion for CLI"""

    The_Curly = re.search(r"\{(.*?)\}", argu)
    The_Brace = re.search(r"\[(.*?)\]", argu)

    if The_Curly is None:
        if The_Brace is None:
            return [o.strip(",") for o in split(argu)]
        else:
            Parse = split(argu[:The_Brace.span()[0]])
            arg = [o.strip(",") for o in Parse]
            arg.append(The_curly.group())
            return arg


class HBNBCommand(cmd.Cmd):
    """The base class for the console"""

    intro = "Welcome to my self written CLI from pYTHON3"""
    prompt = '(hbnb)'

    __Valid_Classes = {"BaseModel", "User", "Review", "Place", "State",
                       "City", "Amenity"}

    def do_EOF(self, argu):
        """
        The EOF function used to exit the CLI\n
        """
        return (True)

    def do_quit(self, argu):
        """
        Quit command to exit the program\n
        """
        return (True)

    def do_create(self, argu):
        """
        Command used to create a new instance of BaseModel\n
        """
        args = parser(argu)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__Valid_Classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, argu):
        """
        Command used to print string representation of an instance
        based on class name and id.\n
        """
        args = parser(argu)
        content = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__Valid_Classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in content:
            print("** no instance found **")
        else:
            print(content["{}.{}".format(args[0], args[1])])

    def do_destroy(self, argu):
        """
        Command used to delete an instance based on class name and id\n
        """
        args = parser(argu)
        content = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__Valid_Classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in content:
            print("** no instance found **")
        else:
            del content["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, argu):
        """
        Command used to print all string representations of an instance
        based or not on the class name.\n
        """
        args = parser(argu)
        content = storage.all()

        if len(args) != 0 and args[0] not in HBNBCommand.__Valid_Classes:
            print("** class doesn't exist **")
        else:
            Obj_Found = []
            for Content in storage.all().values():
                if len(args) > 0 and args[0] == Content.__class__.__name__:
                    Obj_Found.append(Content.__str__())
                elif len(args) == 0:
                    Obj_Found.append(Content.__str__())
            print(Obj_Found)

    def do_update(self, argu):
        """
        Command used to update an instance based on class name and id.\n
        """
        F = False
        args = parser(argu)
        content = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return F
        elif args[0] not in HBNBCommand.__Valid_Classes:
            print("** class doesn't exist **")
            return F
        elif len(args) == 1:
            print("** instance id missing **")
            return F
        elif "{}.{}".format(args[0], args[1]) not in content.keys():
            print("** no instance found **")
            return F
        elif len(args) == 2:
            print("** attribute name missing **")
            return F
        elif len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except ValueError:
                print("** value missing **")
                return F

    def do_clear(self, clear):
        """Function used to clear screen"""
        _ = system('clear')

    def emptyline(self):
        """
        Define what to do when entering a empty line
        """
        pass

    def help(self):
        """
        Help display fucntion used in our cli
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
