import cmd
class HelloWorld(cmd.Cmd):
    """Simple command processor example"""

    FREINDS = ['Alice', 'Adam', 'Barbara', 'Jakobo']
        
    def do_greet(self, person):
        "Greet Person"
        if person and person in self.FREINDS:
            greeting = 'hi, %s!' % person
        elif person:
            greeting = 'Hello, ' + person
        else:
            greeting = 'Hello unnamed person :-)'
        print(greeting)
        
    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FREINDS[:]
        else:
            completions = [
                f
                for f in self.FREINDS
                if f.startswith(text)
            ]
        return completions
        
    def help_greet(self):
        print('\n'.join(['greet [person]', 'Greet named person']))
        
    def do_EOF(self, line):
        return True
    
    def postloop(self):
        print    
        
if __name__ == '__main__':
    HelloWorld().cmdloop()
        