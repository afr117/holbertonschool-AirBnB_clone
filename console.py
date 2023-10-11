#!/usr/bin/env python3
"""
this is a shell in python
"""
import cmd
import shlex
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
        return True

    def do_EOF(self, args):
        """
        Quit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
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
        """
        if not args:
            print("** class name missing **")
            return
        try:
            args_list = shlex.split(args)
            if len(args_list) == 2:
                obj_key = "{}.{}".format(args_list[0], args_list[1])
                obj = storage.all().get(obj_key)
                if obj:
                    print(obj)
                else:
                    print("** no instance found **")
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
                obj_key = "{}.{}".format(args_list[0], args_list[1])
                obj_dict = storage.all()
                if obj_key in obj_dict:
                    del obj_dict[obj_key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        except Exception as e:
            print(e)

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        obj_list = []
        try:
            args_list = shlex.split(args)
            obj_dict = storage.all()
            if len(args_list) == 0:
                for obj in obj_dict.values():
                    obj_list.append(str(obj))
            elif args_list[0] in storage.all_classes:
                for obj in obj_dict.values():
                    if obj.__class__.__name__ == args_list[0]:
                        obj_list.append(str(obj))
            else:
                print("** class doesn't exist **")
                return
            print(obj_list)
        except Exception as e:
            print(e)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        """
        if not args:
            print("** class name missing **")
            return
        try:
            args_list = shlex.split(args)
            obj_dict = storage.all()
            if len(args_list) >= 2:
                obj_key = "{}.{}".format(args_list[0], args_list[1])
                if obj_key in obj_dict:
                    obj = obj_dict[obj_key]
                    if len(args_list) >= 3:
                        attribute = args_list[2]
                        if len(args_list) >= 4:
                            value = args_list[3]
                            try:
                                value = eval(value)
                            except (NameError, SyntaxError):
                                pass
                            setattr(obj, attribute, value)
                            storage.save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

