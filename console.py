#!/usr/bin/python3
"""Console is the entry point of the command interpreter."""

import cmd
import sys
from models.__init__ import storage
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """commandline for the project, HBNB"""
    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """Handles eof to exit"""
        return True

    def do_quit(self, arg):
        """Handles Quit to exit"""
        return True

    def emptyline(self):
        """Does nothiong when its an empty line"""
        pass

    def default(self, arg):
        """When input is invalid, it overrides"""
        cargs = {"show": self.do_show,
                "all": self.do_all,
                "destroy": self.do_destroy}

        arg = (arg.replace("(", ".").replace(")", ".").replace('"', "")
                .replace(",", "").split("."))
        try:
            cmd_new = arg[0] + " " + arg[2]
            func_new = cargs[arg[1]]
            func_new(cmd_new)
        except:
            print("*** Unknown syntax: {}".format(arg))

    def do_create(self, arg):
        """creates a new instance of the commandline interpreter and prints id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg = arg.split()
        inst_new = eval(arg[0])()
        inst_new.save()
        print(inst_new.id)

    def do_show(self, arg):
        """Displays the str rep of a class instance of a given id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return

        arg = arg.split()
        inst_key = arg[0] + "." + arg[1]

        storage = FileStorage()
        storage.reload()
        objs = storage.all()

        try:
            rep_str = objs[inst_key]
            print(rep_str)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance given its cls name and instance id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return

        arg = arg.split()
        inst_key = arg[0] + "." + arg[1]

        storage = FileStorage()
        storage.reload()
        objs = storage.all()

        try:
            del objs[inst_key]
        except KeyError:
            print("** no instance found **")
            storage.save()

    def do_all(self, arg):
        """prints the str rep of all the instances"""
        list1 = []
        list2 = []
        storage = FileStorage()
        storage.reload()
        objs = storage.all()

        for k, v in objs.items():
            list1.append(v.__str__())
        for i in list1:
            list2.append(str(i))
        print(list2)

    def do_count(self, arg):
        """Counts the num of instances of a class"""
        cnt = 0
        for obj in objs.values():
            if arg[0] == obj.__class__.__name__:
                cnt += 1
        print(cnt)

    def do_update(self, arg):
        """updates instances"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        if len(arg) == 3:
            print("** value missing **")
            return

        arg = arg.split()
        inst_key = arg[0] + "." + arg[1]

        storage = FileStorage()
        storage.reload()
        objs = storage.all()

        try:
            val_obj = objs[inst_key]
        except KeyError:
            print("** no instance found**")
            return

        setattr(val_obj, arg[2], arg[3])
        val_obj.save()

    if __name__ == '__main__':
        """prevents the modules running on import"""
        HBNBCommand().cmdloop()
