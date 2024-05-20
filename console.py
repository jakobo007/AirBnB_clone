#!/usr/bin/python3
"""imported modules"""
import cmd
import sys
import os
from models import storage


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter"""

    prompt = '(hbnb) '
    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """To exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass
    
    def do_help(self, arg: str):
        """List available command with 'help' or detailed help with 'help cmd"""
        return cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        
        class_dict = storage.get_class_dict()
        
        if class_name not in class_dict:
            print("** class doesn't exist **")
            return

        cls =  class_dict[class_name]
        new_instance = cls()
        new_instance.save()
        print(new_instance.id)
        
    def do_show(self, arg):
        """Prints the strind representation of an instance"""
        """BAsed on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return 
        if len(args) == 1:
            print("** instance id missing **")
            return

        class_name, instance_id = args[0], args[1]

        class_dict = storage.get_class_dict()

        if class_name not in class_dict:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)

        if instance is None:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        """Changes to be saved to json file"""
        args = arg.split()
        
        if len(args) == 0:
            print("** class name missing **")
            return 
        if len(args) == 1:
            print("** instance id missing **")
            return

        class_name, instance_id = args[0], args[1]

        class_dict = storage.get_class_dict()

        if class_name not in class_dict:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Print all string representation of all instances"""
        """based or not based on the class name"""
        class_dict = storage.get_class_dict()  # Access class_dict from storage
        if arg:
            if arg not in class_dict:
                print("** class doesn't exist **")
                return
            instances = [str(obj) for key, obj in storage.all().items() if key.startswith(arg + ".")]
        else:
            instances = [str(obj) for obj in storage.all().values()]
        print(instances)


    def do_update(self, arg):
        """Updates an instance based on class and id"""
        args = arg.split()
        if len(args) < 4:
            if len(args) == 0:
                print("** class name missing **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            else:
                print("** value missing **")
            return

        class_name, instance_id, attribute, attribute_value = args[0], args[1], args[2], args[3]

        class_dict = storage.get_class_dict()
        
        if class_name not in class_dict:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        
        if instance is None:
            print("** no instance found **")
            return

        try:
            if hasattr(instance, attribute):
                current_value = type(getattr(instance, attribute))
                attribute_type = type(current_value)

                if attribute_type == int:
                    attribute_value = int(attribute_value)
                elif attribute_type == float:
                    attribute_value = float(attribute_value)
                elif attribute_type == str:
                    attribute_value = str(attribute_value)
                setattr(instance, attribute, attribute_value)
                instance.save()
            else:
               setattr(instance, attribute, attribute_value)
        except ValueError:
            print("** invalid value type **")

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
