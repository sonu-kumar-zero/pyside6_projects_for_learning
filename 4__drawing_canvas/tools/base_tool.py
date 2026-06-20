from abc import ABC
from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtWidgets import QGraphicsSceneMouseEvent


class BaseTool(ABC):
    def mouse_press(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None:
        pass

    def mouse_move(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None:
        pass

    def mouse_release(
        self,
        event: QGraphicsSceneMouseEvent,
        scene: QGraphicsScene,
    ) -> None:
        pass