#!/usr/bin/python3
"""imported modules"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter"""

    prompt = '(hbnb)'
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
        try:
            new_instance = eval(arg)()
            new_instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
