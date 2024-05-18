#!/usr/bin/python3
# Imported modules
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter"""

    prompt = '(hbnb)'
    def do_quit(self, arg):
        """Quit command to exit the program"""
        print()
        return True

    def do_EOF(self, arg):
        """To exit the program"""
        print()
        return True

    def do_help(self, arg): 
        """List available commands"""
        if arg:
         return cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
