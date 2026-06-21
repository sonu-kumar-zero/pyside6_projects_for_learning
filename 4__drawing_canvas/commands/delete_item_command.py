from PySide6.QtWidgets import (
    QGraphicsItem,
    QGraphicsScene
)
from commands.command import Command

class DeleteItemCommand(Command):
    def __init__(self, scene: QGraphicsScene, items: list[QGraphicsItem]):
        super().__init__()
        self.scene = scene
        self.items = items

    def execute(self):
        for item in self.items:
            self.scene.removeItem(item)

    def undo(self):
        for item in self.items:
            self.scene.addItem(item)