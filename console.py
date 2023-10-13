#!/usr/bin/python3
"""
The console of the Airbnb project
"""
import cmd
import sys
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Custom console class
    """

    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

    def do_EOF(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        empty lines
        """
        pass

    def do_create(self, line):
        """
         Creates a new instance of BaseModel
        """
        command = self.parseline(line)[0]

        if command is None:
            print("** class name missing **")
        elif command not in self.classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(command)
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """
        Prints the string representation of
        an instance based on the class name and id
        """
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]

        if command is None:
            print("** class name missing **")
        elif command not in self.classes:
            print("** class doesn't exist **")
        elif arg == '':
            print("** instance id missing **")
        else:
            data = storage.all().get(command + '.' + arg)
            if data is None:
                print("** no instance found **")
            else:
                print(data)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]

        if command is None:
            print("** class name missing **")
        elif command not in self.classes:
            print("** class doesn't exist **")
        elif arg == '':
            print("** instance id missing **")
        else:
            key = command + '.' + arg
            data = storage.all().get(key)
            if data is None:
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        command = self.parseline(line)[0]
        objs = storage.all()

        if command is None:
            print([str(objs[obj]) for obj in objs])
        elif command not in self.classes:
            keys = objs.keys()
            print([str(objs[key]) for key in keys if key.startswith(command)])
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    shell = HBNBCommand()
    
    if not sys.stdin.isatty():
        for line in sys.stdin:
            shell.onecmd(line.strip())
    else:
        HBNBCommand().cmdloop()
