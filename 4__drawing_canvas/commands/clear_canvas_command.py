from commands.command import Command
from PySide6.QtWidgets import QGraphicsScene, QGraphicsItem

from items.base_item import BaseItem

class ClearCanvasCommand(Command):
    def __init__(self, scene: QGraphicsScene):
        self.scene = scene
        self.items: list[QGraphicsItem] = [
            item 
            for item in scene.items()
            if isinstance(item, BaseItem) 
        ]
        
    def execute(self):
        for item in self.items:
            self.scene.removeItem(item)
    
    def undo(self):
        for item in self.items:
            self.scene.addItem(item)