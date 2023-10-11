import cmd
from models import storage
from models.user import User

class Console(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg.split()[0]
            if class_name in self.classes:
                new_instance = self.classes[class_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                objects = storage.all()
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                objects = storage.all()
                if key in objects:
                    del objects[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based on the class name"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            args = arg.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects.values() if obj.__class__.__name__ == args[0])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                objects = storage.all()
                if key not in objects:
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    setattr(objects[key], args[2], args[3])
                    storage.save()

    def do_quit(self, arg):
        """Exit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter when reading EOF (Ctrl-D)"""
        print("")
        return True

if __name__ == '__main__':
    console = Console()
    console.cmdloop()

