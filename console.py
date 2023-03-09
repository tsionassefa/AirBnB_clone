#!/usr/bin/python3
import cmd
import sys
import os
import shlex
import models
from models.base_model import BaseModel




class HBNBCommand(cmd.Cmd):
    """HBNB Class """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'BaseModel': BaseModel}
    def do_quit(self, argument):
        """ Defines quit option"""
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True
    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")
    def do_ENTER(self):
        """ Prints help command description """
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
