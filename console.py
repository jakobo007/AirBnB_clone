#!/usr/bin/python3
# Imported modules
import cmd

class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter"""

    prompt = '(hbnb)'
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """To exit the program"""
        return True

    def do_help(self, arg): 
        """List available commands"""
        return cmd.Cmd.do_help(self, arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
