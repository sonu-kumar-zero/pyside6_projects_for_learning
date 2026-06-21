from PySide6.QtCore import QPointF
from PySide6.QtWidgets import QGraphicsItem

from commands.command import Command

class MoveItemCommand(Command):
    def __init__(
        self,
        item: QGraphicsItem,
        new_pos: QPointF,
        old_pos: QPointF,
    ):
        super().__init__()
        self.item = item
        self.new_pos = new_pos
        self.old_pos = old_pos
    
    def execute(self) -> None:
        self.item.setPos(self.new_pos)
    
    def undo(self) -> None:
        self.item.setPos(self.old_pos)