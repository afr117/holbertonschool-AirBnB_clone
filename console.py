#!/usr/bin/env python3
"""
This is a shell in python
"""
import cmd
from models.base_model import BaseModel
from models import storage

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

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Usage: create <class name>
        """
        if not args:
            print("** class name missing **")
            return

        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        if len(args_list) < 2:
            print("** instance id missing **")
            return

        class_name = args_list[0]
        obj_id = args_list[1]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, obj_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        if len(args_list) < 2:
            print("** instance id missing **")
            return

        class_name = args_list[0]
        obj_id = args_list[1]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, obj_id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [class name]
        """
        if not args:
            print([str(obj) for obj in storage.all().values()])
        else:
            class_name = args.split()[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                print([str(obj) for key, obj in storage.all().items() if class_name in key])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        if len(args_list) < 2:
            print("** instance id missing **")
            return

        class_name = args_list[0]
        obj_id = args_list[1]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args_list) < 4:
            print("** attribute name missing **")
            return

        attribute_name = args_list[2]
        if len(args_list) < 5:
            print("** value missing **")
            return

        attribute_value = args_list[3]
        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

