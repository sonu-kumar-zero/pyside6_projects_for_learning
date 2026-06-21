from commands.command import Command

class CommandManager:
    def __init__(self):
        self.undo_stack: list[Command] = []
        self.redo_stack: list[Command] = []
    
    def execute(self, command: Command):
        command.execute()
        
        self.undo_stack.append(command)
        self.redo_stack.clear()
        
    def undo(self):
        if not self.undo_stack:
            return
        
        command = self.undo_stack.pop()
        command.undo()
        
        self.redo_stack.append(command)
        
    def redo(self):
        if not self.redo_stack:
            return
        
        command = self.redo_stack.pop()
        command.execute()
        
        self.undo_stack.append(command)