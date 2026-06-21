from PySide6.QtWidgets import (
    QGraphicsItem,
    QGraphicsScene,
)
from commands.command import Command

class AddItemCommand(Command):
    def __init__(
        self,
        item: QGraphicsItem,
        scene: QGraphicsScene,
    ) -> None:
        self.item = item
        self.scene = scene

    def execute(self) -> None:
        if self.item.scene() is not self.scene:
            self.scene.addItem(self.item)

    def undo(self) -> None:
        if self.item.scene() is self.scene:
            self.scene.removeItem(self.item)