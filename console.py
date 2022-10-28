#!/usr/bin/python3
"""A command line intepreter tool used for AirBnB project"""
import cmd
import readline
import argparse

def parse(argu):
    """Main parsing fucntion for CLI"""
    parser = argparse.ArgumentParser()

    args = parser.parse_args()



class HBNBCommand(cmd.Cmd):
    """The base class for the console"""
    intro = "Welcome to my self written CLI from pYTHON3"""
    prompt = '(hbnb)'
    
    def do_EOF(self, argu):
        """The EOF function used to exit the CLI"""
        return (True)

    def do_quit(self, argu):
        """Quit command to exit the program\n"""
        return (True)

    def emptyline(self):
        """Define what to do when entering a empty line"""
        pass

    def help(self):
        """Help display fucntion used in our cli"""

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
