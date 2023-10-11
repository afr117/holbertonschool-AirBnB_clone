#!/usr/bin/env python3
"""
this is a shell in python
"""
import cmd
import shlex
from models.user import User  # Import the User class
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    A simple command interpreter for the AirBnB project.
    """
    prompt = "(hbnb) "
    
    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        if not args:
            print("** class name missing **")
            return
        try:
            if args == "User":
                new_instance = User()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        except Exception as e:
            print(e)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        if not args:
            print("** class name missing **")
            return
        try:
            args_list = shlex.split(args)
            if len(args_list) == 2:
                if args_list[0] == "User":
                    obj_key = "{}.{}".format(args_list[0], args_list[1])
                    obj = storage.all().get(obj_key)
                    if obj:
                        print(obj)
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        except Exception as e:
            print(e)

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id.
        """
        if not args:
            print("** class name missing **")
            return
        try:
            args_list = shlex.split(args)
            if len(args_list) == 2:
                if args_list[0] == "User":
                    obj_key = "{}.{}".format(args_list[0], args_list[1])
                    obj_dict = storage.all()
                    if obj_key in obj_dict:
                        del obj_dict[obj_key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        except Exception as e:
            print(e)

    # Add methods for 'update' and 'all' specific to the User class

if __name__ == '__main__':
    HBNBCommand().cmdloop()

