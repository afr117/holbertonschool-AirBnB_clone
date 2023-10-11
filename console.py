#!/usr/bin/env python3
"""
this is a shell in python
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    A simple command interpreter for the AirBnB project.
    """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit the program.
        """
        exit()

    def do_EOF(self, args):
        """
        Quit the program.
        """
        self.do_quit(args)

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

