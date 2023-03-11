#!/usr/bin/python3
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

allowed_class = {"BaseModel": BaseModel, "Place": Place, "State": State,
                 "City": City, "Amenity": Amenity, "Review": Review,
                 "User": User}


class HBNBCommand(cmd.Cmd):
    """HBNB Class
    """
    prompt = '(hbnb) '
    def do_quit(self, line):
        """quit command: exit the program"""
        return True

    def do_EOF(self, line):
        """End of File command: exit the program"""
        return True

    def emptyline(self):
        """overridden to not do nothing"""
        pass

    def do_create(self, line):
        """
        this creates a new instance of BaseModel
        """
        new_instance = self.parseline(line)[0]
        if new_instance is None:
            print("** class name missing **")
        elif new_instance not in self.classes:
            print("** class doesn't exist **")
        else:
            new_object = eval(new_instance)()
            new_object.save()
            print(new_object.id)

    def do_show(self, line):
        """
        this prints the string representation of an instance based on
        the class name and id.
        """
        new_instance = self.parseline(line)[0]
        new_instance_id = self.parseline(line)[1]
        if new_instance is None:
            print("** class name missing**")
        elif new_instance not in self.classes:
            print("** class doesn't exist **")
        elif new_instance_id == '':
            print("** instance id missing **")
        else:
            new_instance_data = models.storage.all().get(new_instance + '.' + new_instance_id)
            if new_instance_data is None:
                print("** no instance found **")
            else:
                print(new_instance_data)

    def do_destroy(self, line):
        """
        this deletes an instance based on the class name and id(save the change
        into the JSON file)
        """
        new_instance = self.parseline(line)[0]
        new_instance_id = self.parseline(line)[1]
        if new_instance is None:
            print("** class name missing**")
        elif new_instance not in self.classes:
            print("** class doesn't exist **")
        elif new_instance_id == '':
            print("** instance id missing **")
        else:
            key = new_instance + '.' + new_instance_id
            new_instance_data = models.storage.all().get(key)
            if new_instance_data is None:
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, line):
        """
        this prints all string representation of all instances based or
        not on the class name
        """
        new_instance = self.parseline(line)[0]
        model_objects = models.storage.all()
        if new_instance is None:
            print([str(model_objects[i]) for i in model_objects])
        elif new_instance in self.classes:
            keys = model_objects.keys()
            print([str(model_objects[j]) for j in keys if j.startswith(new_instance)])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        this updates an instance based on the class name and id by adding or updating
        attribute(save the change into the JSON file)
        """
        args = shlex.split(line)
        all_instances = models.storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")

        else:
            if args[0] in classes:
                key = "{}.{}".format(args[0], args[1])

                if key in all_instances:
                    for i, j in all_instances.items():
                        if i == key:
                            setattr(j, args[2], args[3])
                            j.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")


    def count(self, line):
        """
        this prints all string representation of all instances
        """
        objects = models.storage.all()
        if line:
            if line.lower() in self.classes:
                class_objects = {}
                for i in objects:
                    if i.startswith(line):
                        class_objects[i] = objects[i]
                print(len(class_objects))
            else:
                print("** class doesn't exist **")

    def default(self, line):
        """
        this is the default method that checks if command entered has the right
        syntax
        """
        args = line.split(".")
        if len(args) == 2:
            class_name, function = args
            if class_name.lower() in self.classes:
                if function == "all()":
                    self.do_all(class_name)
                elif function == "count()":
                    self.count(class_name)
                elif function.startswith("show"):
                    function = function[5:1]
                    self.do_show(class_name + "" + function)
                elif function.startswith("destroy"):
                    function = function[8:-1]
                    self.do_destroy(class_name + "" + function)
        else:
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
